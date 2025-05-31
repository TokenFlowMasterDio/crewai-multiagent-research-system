import sqlite3
import asyncio
import aiosqlite
from datetime import datetime
from typing import Dict, Any, List, Optional
import json
import os

class DatabaseManager:
    """Manage SQLite database for persistent storage."""
    
    def __init__(self, db_path: str = "crewai_system.db"):
        self.db_path = db_path
        self._initialize_db_sync()  # Initialize synchronously first
    
    def _initialize_db_sync(self):
        """Initialize database tables synchronously."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Crew executions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS crew_executions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    topic TEXT NOT NULL,
                    result TEXT NOT NULL,
                    execution_time REAL,
                    timestamp DATETIME NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # QA interactions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS qa_interactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Agent memories table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS agent_memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    agent_type TEXT NOT NULL,
                    memory_data TEXT NOT NULL,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
            conn.close()
            print("✅ Database initialized successfully")
            
        except Exception as e:
            print(f"❌ Error initializing database: {e}")
    
    async def save_crew_execution(self, session_id: str, topic: str, result: str, 
                                execution_time: float = None, timestamp: datetime = None):
        """Save crew execution results."""
        try:
            if timestamp is None:
                timestamp = datetime.now()
            
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    "INSERT INTO crew_executions (session_id, topic, result, execution_time, timestamp) VALUES (?, ?, ?, ?, ?)",
                    (session_id, topic, result, execution_time, timestamp)
                )
                await db.commit()
        except Exception as e:
            print(f"Error saving crew execution: {e}")
    
    async def save_qa_interaction(self, session_id: str, question: str, answer: str):
        """Save Q&A interaction."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    "INSERT INTO qa_interactions (session_id, question, answer) VALUES (?, ?, ?)",
                    (session_id, question, answer)
                )
                await db.commit()
        except Exception as e:
            print(f"Error saving QA interaction: {e}")
    
    async def save_agent_memory(self, session_id: str, agent_type: str, memory_data: str):
        """Save agent memory state."""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                # Update existing or insert new
                await db.execute(
                    "INSERT OR REPLACE INTO agent_memories (session_id, agent_type, memory_data, updated_at) VALUES (?, ?, ?, ?)",
                    (session_id, agent_type, memory_data, datetime.now())
                )
                await db.commit()
        except Exception as e:
            print(f"Error saving agent memory: {e}")
    
    def get_agent_memory(self, session_id: str, agent_type: str) -> Optional[str]:
        """Get agent memory data synchronously."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute(
                "SELECT memory_data FROM agent_memories WHERE session_id = ? AND agent_type = ? ORDER BY updated_at DESC LIMIT 1",
                (session_id, agent_type)
            )
            result = cursor.fetchone()
            conn.close()
            
            return result[0] if result else None
        except Exception as e:
            print(f"Error getting agent memory: {e}")
            return None
    
    def get_session_history(self, session_id: str) -> Dict[str, Any]:
        """Get complete session history."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get crew executions
            cursor.execute(
                "SELECT topic, result, timestamp FROM crew_executions WHERE session_id = ? ORDER BY timestamp DESC LIMIT 10",
                (session_id,)
            )
            executions = cursor.fetchall()
            
            # Get QA interactions
            cursor.execute(
                "SELECT question, answer, timestamp FROM qa_interactions WHERE session_id = ? ORDER BY timestamp DESC LIMIT 10",
                (session_id,)
            )
            qa_interactions = cursor.fetchall()
            
            conn.close()
            
            return {
                "executions": [{"topic": e[0], "result": e[1][:200] + "...", "timestamp": e[2]} for e in executions],
                "qa_interactions": [{"question": q[0], "answer": q[1][:200] + "...", "timestamp": q[2]} for q in qa_interactions],
                "total_executions": len(executions),
                "total_qa": len(qa_interactions)
            }
        except Exception as e:
            print(f"Error getting session history: {e}")
            return {"error": str(e)}
