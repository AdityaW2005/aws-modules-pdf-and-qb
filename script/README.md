# 🔄 PDF to Clean Text Converter for LLM Question Generation

This directory contains a specialized PDF conversion tool designed to transform AWS Academy study guides into clean, LLM-readable text files for automated question bank generation.

## 🎯 Purpose

Large Language Models (LLMs) cannot directly read PDF files, but they excel at generating educational content from well-structured text. This converter bridges that gap by:

1. **Extracting** text content from AWS Academy PDF study guides
2. **Cleaning** repetitive elements (copyright notices, headers, footers)
3. **Formatting** content for optimal LLM comprehension
4. **Organizing** output for question generation workflows

## 📁 Directory Structure

```
script/
├── convert.py           # Main conversion script
├── text/               # Output directory for clean text files
│   ├── M01SG_clean.txt # Module 1: Cloud Concepts Overview
└── README.md           # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Access to the `../pdfs/` directory containing AWS Academy PDFs

### Usage

```bash
# Navigate to the script directory
cd script/

# Run the converter (auto-installs dependencies)
python3 convert.py
```

That's it! The script will:
- ✅ Auto-install required packages (`pdfplumber`, `PyPDF2`)
- ✅ Find all PDF files in `../pdfs/` directory
- ✅ Convert each PDF to clean text
- ✅ Save cleaned files to `text/` directory
- ✅ Provide progress feedback and summary

## 🧹 Text Cleaning Features

The converter performs intelligent cleaning to make content LLM-friendly:

### Removes Repetitive Content
- Copyright notices: `© 2022, Amazon Web Services, Inc...`
- Trademark statements: `All trademarks are the property of their owners`
- Course codes: `100-ACCLFO-20-EN-SG`
- Repetitive headers and footers

### Improves Formatting
- Consolidates multiple blank lines
- Removes table extraction artifacts
- Eliminates page numbering noise
- Preserves meaningful content structure

### Preserves Important Content
- ✅ All educational material
- ✅ Key concepts and definitions
- ✅ Examples and use cases
- ✅ Section organization
- ✅ Page references for context

## 🤖 LLM Integration Benefits

The cleaned text files are optimized for LLM question generation because they:

1. **Focus on Content**: Removed distractions help LLMs identify key concepts
2. **Maintain Context**: Page markers and structure preservation aid comprehension
3. **Reduce Noise**: Clean text improves question relevance and accuracy
4. **Enable Automation**: Consistent format allows batch processing

## 📊 Example Output

### Before Cleaning (Raw PDF Extract)
```
AWS Training and Certification Module 1: Cloud Concepts Overview
© 2022, Amazon Web Services, Inc. or its affiliates. All rights reserved.
What is cloud computing?
© 2022, Amazon Web Services, Inc. or its affiliates. All rights reserved. 5
Cloud computing is the on-demand delivery...
[TABLES FOUND ON THIS PAGE]
Table 1: ...
© 2022, Amazon Web Services, Inc. or its affiliates. All rights reserved. 8
```

### After Cleaning (LLM-Ready)
```
=== Page 8 ===
What is cloud computing?

Cloud computing is the on-demand delivery of compute power, database, storage, 
applications, and other IT resources via the internet with pay-as-you-go pricing.
```

## 🔧 Technical Details

### PDF Processing Methods
1. **Primary**: `pdfplumber` - Superior handling of formatted content and tables
2. **Fallback**: `PyPDF2` - Reliable text extraction for simpler PDFs
3. **Error Handling**: Graceful degradation and informative error messages

### Text Processing Pipeline
```
PDF Input → Text Extraction → Pattern Cleaning → Format Optimization → LLM-Ready Output
```

### Cleaning Patterns
- Regular expressions for copyright/trademark removal
- Line-by-line filtering for headers/footers
- Multi-line consolidation for readability
- Content preservation with noise reduction

## 🛠️ Troubleshooting

### Common Issues

**No PDFs Found**
```
❌ No PDF files found in ../pdfs/
```
- Ensure PDF files are in the correct `pdfs/` directory
- Check file permissions

**Package Installation Fails**
```
📦 Installing pdfplumber...
```
- Ensure `pip3` is available
- Try manual installation: `pip3 install pdfplumber PyPDF2`

**Poor Text Quality**
- Some PDFs may be image-based (scanned documents)
- Consider OCR tools for image-heavy PDFs
- Check if original PDF is text-selectable

### Performance Tips
- Processing 50-page PDFs typically takes 30-60 seconds
- Large batches may benefit from parallel processing
- Clean text files are ~70% smaller than raw extracts

## 🔄 Workflow Integration

### Typical LLM Question Generation Workflow
1. **Convert**: `python3 convert.py`
2. **Review**: Check `text/` directory for clean files
3. **Prompt**: Use cleaned content with LLM APIs
4. **Generate**: Create question banks automatically
5. **Validate**: Review and refine generated questions

### Example LLM Prompts
```
"Using the following AWS study guide content, generate 15 multiple-choice questions 
with varying difficulty levels (5 easy, 7 medium, 3 hard). Include answers and brief 
explanations. Focus on practical application scenarios..."
```

## 📝 Output Format

Each cleaned text file includes:
- **Header**: Source file name, processing date, purpose
- **Content**: Clean, structured text with page markers
- **Encoding**: UTF-8 for universal compatibility
- **Naming**: `{OriginalName}_clean.txt` format

## 🎓 Educational Value

This converter enables:
- **Automated Content Processing**: Scale question creation across multiple modules
- **Consistent Quality**: Standardized cleaning ensures uniform LLM input
- **Rapid Iteration**: Quick conversion allows fast content updates
- **Knowledge Extraction**: Transform static PDFs into dynamic learning resources

---

**Ready to generate comprehensive AWS question banks with LLM assistance!** 🚀
