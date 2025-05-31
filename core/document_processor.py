import os
from pathlib import Path
from typing import Dict, Any, Optional
import asyncio

class DocumentProcessor:
    """Simple document processing."""
    
    def __init__(self, settings):
        self.settings = settings
    
    async def process_document(self, file_path: str) -> str:
        """Process document and return text content."""
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            
            file_extension = Path(file_path).suffix.lower()
            
            if file_extension == '.txt':
                return await self._process_text(file_path)
            elif file_extension == '.pdf':
                return await self._process_pdf(file_path)
            else:
                return f"File type {file_extension} not yet supported. Currently supports: .txt, .pdf"
                
        except Exception as e:
            raise Exception(f"Error processing document: {str(e)}")
    
    async def _process_text(self, file_path: str) -> str:
        """Process text document."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if not content.strip():
                return "Text file is empty"
            
            return content
            
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='latin-1') as file:
                    return file.read()
            except Exception:
                return "Could not read file - encoding issues"
        except Exception as e:
            raise Exception(f"Error processing text file: {str(e)}")
    
    async def _process_pdf(self, file_path: str) -> str:
        """Process PDF document."""
        try:
            # Try to use PyMuPDF if available
            import fitz
            doc = fitz.open(file_path)
            text_content = []
            
            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text()
                if text.strip():
                    text_content.append(f"Page {page_num + 1}:\n{text}\n")
            
            doc.close()
            
            if not text_content:
                return "No text content found in PDF"
            
            return "\n".join(text_content)
            
        except ImportError:
            return "PDF processing not available. Install PyMuPDF: pip install PyMuPDF"
        except Exception as e:
            return f"Error processing PDF: {str(e)}"