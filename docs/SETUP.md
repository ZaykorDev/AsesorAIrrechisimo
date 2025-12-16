# Setup Guide

Complete installation and configuration guide for El Asesor AIrrecho.

## System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 20.04+)
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum
- **Internet**: Required for AI API calls and web search

### Recommended
- **Python**: 3.11+
- **RAM**: 4GB+
- **Browser**: Chrome, Firefox, Safari, or Edge (latest versions)

## Step-by-Step Installation

### 1. Install Python

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run installer
3. **IMPORTANT**: Check "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
```cmd
   python --version
```

#### macOS
```bash
# Using Homebrew (recommended)
brew install python@3.11

# Verify
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3-pip

# Verify
python3 --version
```

### 2. Clone the Repository
```bash
# Using HTTPS
git clone https://github.com/sdelmo/vz-portfolio-manager.git

# Or using SSH
git clone git@github.com:sdelmo/vz-portfolio-manager.git

# Navigate to directory
cd portfolio-manager
```

### 3. Set Up Virtual Environment (Recommended)

#### Why use a virtual environment?
- Isolates project dependencies
- Prevents conflicts with other Python projects
- Makes the project portable

#### Create and activate:

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

**What gets installed:**
- `streamlit>=1.31.0` - Web framework
- `anthropic>=0.18.0` - Claude AI API client
- `pandas>=2.0.0` - Data manipulation

### 5. Get Your Anthropic API Key

1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to "API Keys"
4. Click "Create Key"
5. Copy the key (starts with `sk-ant-`)
6. **Save it securely** - you'll need it to run the app

#### Add API Credits
1. Go to "Billing" in the Anthropic console
2. Add payment method
3. Add credits: $20-50 recommended for 4-12 months of regular use

### 6. Run the Application
```bash
streamlit run portfolio_manager.py
```

The app will automatically open in your browser at `http://localhost:8501`

If it doesn't open automatically:
- Open your browser
- Go to `http://localhost:8501`

### 7. First-Time Configuration

1. **Enter API Key**
   - In the sidebar, paste your Anthropic API key
   - It's stored only in session memory (not saved permanently)

2. **Set Risk Profile**
   - Choose: Conservador, Moderado, or Agresivo
   - Or select "Personalizado" for custom preferences

3. **Add Your First Holding**
   - Go to "Manejo del Portafolio" tab
   - Click "Agregar Nuevo Holding"
   - Fill in: Symbol, Name, Type, Quantity, Price

4. **Start Chatting**
   - Go to "Habla con el Venezolano" tab
   - Ask: "¿Cómo está mi portafolio?"
   - Enjoy! 🎉

## Troubleshooting

### Common Issues

#### "Python not found" or "Command not found"

**Cause**: Python not in PATH

**Solution**:
- Windows: Reinstall Python, ensure "Add to PATH" is checked
- macOS/Linux: Use full path `/usr/bin/python3` or add to PATH

#### "Module not found: streamlit"

**Cause**: Dependencies not installed

**Solution**:
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt

# Or install individually
pip install streamlit anthropic pandas
```

#### "Port 8501 is already in use"

**Cause**: Another Streamlit app is running

**Solution**:
```bash
# Option 1: Close other terminal windows
# Option 2: Use different port
streamlit run portfolio_manager.py --server.port 8502
```

#### "Invalid API key" Error

**Cause**: API key incorrect or expired

**Solution**:
- Check you copied the full key (starts with `sk-ant-`)
- Verify key at [console.anthropic.com](https://console.anthropic.com/)
- Generate a new key if needed

#### App loads but doesn't respond

**Cause**: API credits depleted or network issue

**Solution**:
- Check API credits in Anthropic console
- Verify internet connection
- Check Anthropic status page

#### Venezuelan personality not working (sounds formal)

**Cause**: Bug in system prompt handling (fixed in latest version)

**Solution**:
- Make sure you have the latest `portfolio_manager.py`
- Clear chat history (button in sidebar)
- Restart the app
- See [BUG_FIX_CRITICO.md](../BUG_FIX_CRITICO.md) for details

## Advanced Configuration

### Environment Variables (Optional)

Instead of entering API key each time, create a `.env` file:
```bash
# .env file
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Then modify `portfolio_manager.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('ANTHROPIC_API_KEY', '')
```

**⚠️ Remember**: Add `.env` to `.gitignore`!

### Custom Port
```bash
streamlit run portfolio_manager.py --server.port 8080
```

### Disable CORS (for development)
```bash
streamlit run portfolio_manager.py --server.enableCORS false
```

### Auto-reload on File Changes
```bash
streamlit run portfolio_manager.py --server.runOnSave true
```

## Creating Desktop Shortcuts

### Windows

Create file `Portfolio Manager.bat`:
```batch
@echo off
cd "C:\path\to\portfolio-manager"
call venv\Scripts\activate
streamlit run portfolio_manager.py
pause
```

### macOS

Create file `Portfolio Manager.command`:
```bash
#!/bin/bash
cd "/path/to/portfolio-manager"
source venv/bin/activate
streamlit run portfolio_manager.py
```

Make executable:
```bash
chmod +x "Portfolio Manager.command"
```

### Linux

Create file `portfolio-manager.desktop`:
```ini
[Desktop Entry]
Type=Application
Name=Portfolio Manager
Exec=/path/to/portfolio-manager/venv/bin/streamlit run /path/to/portfolio-manager/portfolio_manager.py
Terminal=false
Icon=/path/to/icon.png
```

## Updating the Application
```bash
# Pull latest changes
git pull origin main

# Update dependencies (if changed)
pip install -r requirements.txt --upgrade

# Restart the app
streamlit run portfolio_manager.py
```

## Uninstalling
```bash
# Deactivate virtual environment
deactivate

# Remove directory
cd ..
rm -rf portfolio-manager

# Or on Windows
rd /s /q portfolio-manager
```

## Getting Help

If you encounter issues:

1. **Check this guide** - Most common issues are covered
2. **Check GitHub Issues** - Someone may have had the same problem
3. **Read error messages** - They usually indicate the problem
4. **Enable debug mode**:
```bash
   streamlit run portfolio_manager.py --logger.level=debug
```
5. **Open an issue** - Provide error messages and system info

## Next Steps

- [Feature Guide](FEATURES.md) - Learn about all features
- [Usage Examples](EXAMPLES.md) - See example interactions
- [Main README](../README.md) - Project overview

---

**Need more help?** Open an issue on GitHub or check the main README.