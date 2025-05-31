from typing import Dict, Optional
import json

# Simple memory implementation that doesn't require langchain initially
class SimpleMemory:
    """Simple memory implementation."""
    
    def __init__(self):
        self.messages = []
        self.memory_key = "chat_history"
    
    def add_message(self, message):
        """Add a message to memory."""
        self.messages.append(str(message))
    
    def clear(self):
        """Clear memory."""
        self.messages = []
    
    def get_messages(self):
        """Get all messages."""
        return self.messages

class PersistentMemoryManager:
    """Enhanced memory manager with database persistence."""
    
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self._memory_cache: Dict[str, SimpleMemory] = {}
    
    def get_agent_memory(self, session_id: str, agent_type: str):
        """Get or create agent memory with persistence."""
        cache_key = f"{session_id}_{agent_type}"
        
        if cache_key not in self._memory_cache:
            # Try to use langchain memory if available, otherwise use simple memory
            try:
                from langchain.memory import ConversationBufferMemory
                memory = ConversationBufferMemory(
                    memory_key="chat_history",
                    return_messages=True,
                    output_key="output"
                )
            except ImportError:
                print("Using simple memory (langchain not available)")
                memory = SimpleMemory()
            
            self._memory_cache[cache_key] = memory
        
        return self._memory_cache[cache_key]
    
    def clear_session_memory(self, session_id: str):
        """Clear all memory for a session."""
        keys_to_remove = [key for key in self._memory_cache.keys() if key.startswith(session_id)]
        for key in keys_to_remove:
            if hasattr(self._memory_cache[key], 'clear'):
                self._memory_cache[key].clear()