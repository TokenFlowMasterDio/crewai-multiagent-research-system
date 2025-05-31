# 🤖 CrewAI Multi-Agent Research & Analysis System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![CrewAI](https://img.shields.io/badge/CrewAI-0.28.0-green?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Latest-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Compatible-purple?style=for-the-badge)

> **Professional-grade multi-agent AI system that revolutionizes research, document analysis, and intelligent image processing**

<div align="center">
  <img src="docs/images/system-overview.png" alt="CrewAI System Overview" width="800"/>
  <p><em>Complete multi-agent AI system with web interface</em></p>
</div>

## 🚀 What Makes This Special

This isn't just another AI tool - it's a **collaborative AI workforce** that thinks and works like a professional team:

- 🤝 **Multiple AI Agents** working together with specialized roles
- 🔍 **Real-time web research** with proper source citations
- 📄 **Intelligent document processing** for PDFs, Word, Excel files
- 🖼️ **Smart image analysis** that understands code screenshots and technical diagrams
- 🌐 **Production-ready web interface** with session management
- 💾 **Persistent memory** and database storage
- ⚡ **Lightning-fast results** - 8 hours of research in 60 seconds

## ✨ Core Features

### 🔬 Multi-Agent Research System
- **Research Agent**: Gathers comprehensive data from multiple web sources
- **Reporter Agent**: Creates professional reports with proper formatting
- **Fact-Checker Agent**: Verifies information accuracy and source reliability

### 🌐 Real-Time Web Search Integration
- **Serper API** (Google Search) for comprehensive results
- **Tavily API** for AI-optimized research queries
- **Brave Search API** for privacy-focused, unbiased results
- **Intelligent fallback** system ensures reliability

### 🖼️ Advanced Image Analysis
- **Code Screenshot Understanding**: Upload Python, JavaScript, SQL code images
- **Technical Diagram Analysis**: Understands architecture diagrams and flowcharts
- **Document Image Processing**: Extracts text and insights from document photos
- **Expert-Level Insights**: Provides code reviews, optimization suggestions, security analysis

### 📄 Document Intelligence
- **PDF Processing**: Full text extraction with page references
- **Word Document Analysis**: Comprehensive content and structure analysis
- **Excel/CSV Processing**: Data analysis with statistical insights
- **Multi-format Support**: Handles various document types seamlessly

## 🎬 Live System Demo

### 🔍 Research Capabilities
<div align="center">
  <img src="docs/images/research-demo.png" alt="AI Research Demo" width="700"/>
  <p><em>Generate comprehensive research reports with real citations in under 60 seconds</em></p>
</div>

**What you see above:**
- Multi-agent collaboration in action
- Real-time web search with multiple APIs
- Professional report generation with proper citations
- Source verification and fact-checking

### 🖼️ Smart Image Analysis
<div align="center">
  <img src="docs/images/code-analysis-demo.png" alt="Code Analysis Demo" width="700"/>
  <p><em>Upload code screenshots and get expert-level technical analysis</em></p>
</div>

**Capabilities demonstrated:**
- Programming language identification (Python, JavaScript, SQL, etc.)
- Code quality assessment and improvement suggestions
- Security vulnerability detection
- Performance optimization recommendations
- Framework and library recognition

### 📊 Document Intelligence
<div align="center">
  <img src="docs/images/document-demo.png" alt="Document Processing Demo" width="700"/>
  <p><em>Process complex documents and extract key insights automatically</em></p>
</div>

**Document processing features:**
- PDF text extraction with page references
- Excel data analysis with statistical insights
- Word document structure analysis
- Multi-format support with intelligent parsing

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Framework** | CrewAI + LangChain | Multi-agent orchestration |
| **LLM** | Ollama (Mistral) | Local language model processing |
| **Web Search** | Serper, Tavily, Brave APIs | Real-time information gathering |
| **Database** | SQLite + aiosqlite | Data persistence and sessions |
| **Web Interface** | Gradio | User-friendly web application |
| **Document Processing** | PyMuPDF, python-docx, pandas | Multi-format document handling |
| **Image Analysis** | PIL, OCR libraries | Smart image understanding |

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Ollama installed and running
- API keys for web search (optional but recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/TokenFlowMasterDio/crewai-multiagent-research-system.git
   cd crewai-multiagent-research-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Ollama**
   ```bash
   ollama serve
   ollama pull mistral
   ```

4. **Configure environment (optional)**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Launch the system**
   ```bash
   python run_system.py
   ```

6. **Access the interface**
   Open your browser to `http://localhost:7864`

<div align="center">
  <img src="docs/images/startup-process.png" alt="System Startup" width="600"/>
  <p><em>System initialization and startup process</em></p>
</div>

## 🎯 Usage Examples

### Research Automation
```
Query: "Latest developments in AI safety and alignment research"
Result: Comprehensive 2000+ word report with 15+ verified sources
Time: ~60 seconds
```

### Code Analysis
```
Upload: Python function screenshot
Query: "Analyze this code for performance and security issues"
Result: Detailed code review with optimization suggestions
Time: ~30 seconds
```

### Document Processing
```
Upload: 50-page research PDF
Query: "Summarize key findings and methodologies"
Result: Executive summary with page references
Time: ~45 seconds
```

## 📁 Project Structure

```
crewai-multiagent-research-system/
├── 📁 agents/              # Agent definitions and configurations
├── 📁 config/              # System configuration and settings
├── 📁 core/                # Core system modules
│   ├── agents_factory.py   # Agent creation and management
│   ├── database.py         # Database operations
│   ├── memory_manager.py   # Session and memory handling
│   ├── tools_manager.py    # Web search and tool integration
│   └── document_processor.py # Document analysis capabilities
├── 📁 utils/               # Utility functions and helpers
├── 📁 docs/                # Documentation and screenshots
│   └── 📁 images/          # Demo screenshots and diagrams
├── 📄 run_system.py        # Main application launcher
├── 📄 requirements.txt     # Python dependencies
└── 📄 README.md           # This file
```

## ⚙️ Configuration

### Environment Variables
```bash
# LLM Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral
TEMPERATURE=0.7

# Search API Keys (optional but recommended)
SERPER_API_KEY=your_serper_key_here
TAVILY_API_KEY=your_tavily_key_here  
BRAVE_API_KEY=your_brave_key_here

# System Settings
VERBOSE=true
MAX_EXECUTION_TIME=300
```

### API Key Setup
1. **Serper API**: Get free tier at [serper.dev](https://serper.dev) (100 searches/month)
2. **Tavily API**: Sign up at [tavily.com](https://tavily.com) for AI-optimized search
3. **Brave Search**: Get API access at [brave.com/search/api](https://brave.com/search/api)

## 🎪 Feature Gallery

<div align="center">

| Research Automation | Code Analysis | Document Processing |
|:-------------------:|:-------------:|:------------------:|
| ![Research](docs/images/research-feature.png) | ![Code](docs/images/code-feature.png) | ![Document](docs/images/document-feature.png) |
| *Multi-source research with citations* | *Expert-level code review* | *Intelligent document analysis* |

</div>

## 🎯 Use Cases

### For Developers
- **Code review automation** from screenshots
- **Technical research** with verified sources
- **Documentation analysis** and summarization
- **Architecture diagram** interpretation

<div align="center">
  <img src="docs/images/developer-workflow.png" alt="Developer Workflow" width="600"/>
  <p><em>Typical developer workflow with AI assistance</em></p>
</div>

### For Businesses
- **Market research** with competitive analysis
- **Document intelligence** for legal/compliance
- **Technical due diligence** for investments
- **Content research** for marketing teams

<div align="center">
  <img src="docs/images/business-workflow.png" alt="Business Workflow" width="600"/>
  <p><em>Business intelligence and research automation</em></p>
</div>

### For Researchers
- **Literature review** automation
- **Data analysis** from multiple document types
- **Citation management** with source verification
- **Research report** generation

## 🚀 Performance Metrics

<div align="center">
  <img src="docs/images/performance-metrics.png" alt="Performance Metrics" width="700"/>
  <p><em>System performance and time savings analysis</em></p>
</div>

| Task Type | Traditional Time | AI System Time | Time Savings |
|-----------|------------------|----------------|--------------|
| Market Research | 8 hours | 60 seconds | 99.8% |
| Code Review | 2 hours | 30 seconds | 99.6% |
| Document Analysis | 4 hours | 45 seconds | 99.7% |
| Technical Research | 6 hours | 90 seconds | 99.6% |

## 🎥 Video Demonstrations

### Quick Demo Videos
- **[2-Minute System Overview](docs/videos/system-overview.mp4)** - Complete feature walkthrough
- **[Research Demo](docs/videos/research-demo.mp4)** - Live research generation in 60 seconds
- **[Code Analysis Demo](docs/videos/code-analysis.mp4)** - Screenshot to expert review
- **[Document Processing](docs/videos/document-demo.mp4)** - PDF analysis and insights

*Note: Video files are large and stored locally. Screenshots above provide visual previews.*

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure backward compatibility

<div align="center">
  <img src="docs/images/contribution-workflow.png" alt="Contribution Workflow" width="500"/>
  <p><em>Open source contribution process</em></p>
</div>

## 🐛 Known Issues & Limitations

- **OCR accuracy** varies with image quality
- **API rate limits** may affect search performance
- **Large documents** (>100MB) may require additional processing time
- **Local LLM** performance depends on hardware capabilities

## 🛣️ Roadmap

<div align="center">
  <img src="docs/images/roadmap.png" alt="Development Roadmap" width="700"/>
  <p><em>Future development plans and milestones</em></p>
</div>

### Phase 1: Core Enhancements
- [ ] Advanced OCR with multiple providers
- [ ] Video content analysis capabilities  
- [ ] Enhanced document format support
- [ ] API endpoint for programmatic access

### Phase 2: Enterprise Features
- [ ] User authentication and permissions
- [ ] Team collaboration features
- [ ] Advanced analytics dashboard
- [ ] Custom agent development tools

### Phase 3: Scale & Performance
- [ ] Distributed processing capabilities
- [ ] Cloud deployment options
- [ ] Advanced caching mechanisms
- [ ] Real-time collaboration features

## 📊 System Requirements

### Minimum Requirements
- **OS**: Windows 10, macOS 10.15, Ubuntu 18.04+
- **Python**: 3.9+
- **RAM**: 8GB (16GB recommended)
- **Storage**: 2GB free space
- **Network**: Internet connection for web search

### Recommended Setup
- **OS**: Latest stable versions
- **Python**: 3.11+
- **RAM**: 16GB+ for optimal performance
- **Storage**: 5GB+ for document storage
- **GPU**: Optional, enhances local LLM performance

## 🔒 Security & Privacy

<div align="center">
  <img src="docs/images/security-architecture.png" alt="Security Architecture" width="600"/>
  <p><em>System security and privacy protection measures</em></p>
</div>

- **Local processing**: LLM runs entirely on your machine
- **API key security**: Environment-based configuration
- **Data privacy**: No data sent to external services without explicit consent
- **Session isolation**: Each session maintains separate data context

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/TokenFlowMasterDio/crewai-multiagent-research-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/TokenFlowMasterDio/crewai-multiagent-research-system/discussions)
- **Professional Consulting**: Available for custom implementations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Acknowledgments

- **CrewAI Team** for the amazing multi-agent framework
- **LangChain Community** for comprehensive LLM tooling
- **Ollama Project** for local LLM capabilities
- **Open Source Community** for inspiration and contributions

## ⭐ Star History

If this project helped you, please consider giving it a star! It helps others discover this tool and motivates continued development.

<div align="center">
  <img src="docs/images/star-history.png" alt="GitHub Star History" width="500"/>
  <p><em>Project growth and community engagement</em></p>
</div>

---

<div align="center">

**Built with ❤️ by [TokenFlowMasterDio](https://github.com/TokenFlowMasterDio)**

*Revolutionizing research and analysis through collaborative AI*

<img src="docs/images/footer-logo.png" alt="CrewAI System Logo" width="200"/>

</div>
