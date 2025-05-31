import gradio as gr
import asyncio
import uuid
import json
import os
from typing import Dict, Any, Tuple, Optional
import plotly.graph_objs as go
from datetime import datetime, timedelta

class GradioInterface:
    """Advanced Gradio web interface for CrewAI system."""
    
    def __init__(self, crewai_system):
        self.system = crewai_system
        self.active_sessions: Dict[str, str] = {}
        
    def create_interface(self) -> gr.Blocks:
        """Create the main Gradio interface."""
        
        with gr.Blocks(
            title="CrewAI Production System",
            theme=gr.themes.Soft()
        ) as interface:
            
            session_id = gr.State(value=lambda: str(uuid.uuid4()))
            
            with gr.Row():
                gr.HTML("<h1>🤖 CrewAI Production System</h1>")
            
            with gr.Tabs():
                # Research Tab
                with gr.Tab("🔍 AI Research"):
                    research_topic = gr.Textbox(
                        label="Research Topic",
                        placeholder="Enter a topic for AI research",
                        lines=2
                    )
                    research_btn = gr.Button("🚀 Start Research", variant="primary")
                    research_output = gr.Textbox(
                        label="Research Results",
                        lines=20,
                        show_copy_button=True
                    )
                
                # Document Q&A Tab
                with gr.Tab("📄 Document Q&A"):
                    file_upload = gr.File(
                        label="Upload Document",
                        file_types=[".pdf", ".docx", ".txt"]
                    )
                    qa_question = gr.Textbox(
                        label="Question",
                        placeholder="Ask about the document"
                    )
                    qa_btn = gr.Button("💬 Ask Question")
                    qa_output = gr.Textbox(label="Answer", lines=10)
            
            # Event handlers
            research_btn.click(
                fn=self._handle_research,
                inputs=[research_topic, session_id],
                outputs=[research_output]
            )
            
            qa_btn.click(
                fn=self._handle_document_qa,
                inputs=[file_upload, qa_question, session_id],
                outputs=[qa_output]
            )
        
        return interface
    
    def _handle_research(self, topic: str, session_id: str) -> str:
        """Handle research request."""
        if not topic.strip():
            return "Please enter a research topic."
        
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(
                self.system.create_research_crew(topic, session_id)
            )
            loop.close()
            return result
        except Exception as e:
            return f"Research failed: {str(e)}"
    
    def _handle_document_qa(self, file, question: str, session_id: str) -> str:
        """Handle document Q&A request."""
        if not file or not question.strip():
            return "Please upload a document and enter a question."
        
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(
                self.system.process_document_qa(file.name, question, session_id)
            )
            loop.close()
            return result
        except Exception as e:
            return f"Document Q&A failed: {str(e)}"