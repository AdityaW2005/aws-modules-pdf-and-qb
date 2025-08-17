#!/usr/bin/env python3
"""
PDF to Clean Text Converter for LLM Question Generation

This script converts PDF files to clean, LLM-friendly text files by:
1. Extracting text from PDFs using multiple methods (pdfplumber + PyPDF2 fallback)
2. Cleaning repetitive content (copyright notices, footers, etc.)
3. Organizing content for better LLM comprehension
4. Outputting clean text files ready for question generation

Author: AWS Academy Question Bank Project
Purpose: Enable LLMs to read AWS study guides and generate comprehensive question banks
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime


def install_required_packages():
    """Install required packages if not available"""
    packages = ["pdfplumber", "PyPDF2"]

    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"📦 Installing {package}...")
            os.system(f"pip3 install {package}")


def clean_text_content(text):
    """
    Clean extracted text by removing repetitive content and improving formatting
    """
    # Common patterns to remove
    patterns_to_remove = [
        r"© \d{4}, Amazon Web Services, Inc\. or its affiliates\. All rights reserved\..*?\d*",
        r"All trademarks are the property of their owners\.",
        r"AWS Training and Certification.*?Module \d+:.*?Overview",
        r"\d+-[A-Z]+-\d+-[A-Z]+-[A-Z]+",  # Course codes like 100-ACCLFO-20-EN-SG
        r"This work may not be reproduced.*?prohibited\.",
        r"Commercial copying, lending, or selling is prohibited\.",
        r"\[TABLES FOUND ON THIS PAGE\]",
        r"Table \d+:[\s\S]*?(?=\n\n|\n--- Page|\n[A-Z])",  # Remove table extractions
    ]

    cleaned_text = text

    # Remove each pattern
    for pattern in patterns_to_remove:
        cleaned_text = re.sub(
            pattern, "", cleaned_text, flags=re.MULTILINE | re.IGNORECASE
        )

    # Clean up page headers and footers
    lines = cleaned_text.split("\n")
    cleaned_lines = []

    for line in lines:
        line = line.strip()

        # Skip empty lines and very short lines that are likely artifacts
        if len(line) < 3:
            continue

        # Skip lines that are just page numbers or navigation
        if re.match(r"^\d+$", line):
            continue

        # Skip repetitive AWS branding lines
        if any(
            skip_phrase in line.lower()
            for skip_phrase in [
                "aws academy cloud foundations",
                "module 1: cloud concepts overview",
                "aws training and certification",
            ]
        ):
            continue

        cleaned_lines.append(line)

    # Join lines back and clean up multiple newlines
    cleaned_text = "\n".join(cleaned_lines)
    cleaned_text = re.sub(r"\n{3,}", "\n\n", cleaned_text)

    return cleaned_text.strip()


def extract_with_pdfplumber(pdf_path):
    """Extract text using pdfplumber (better for formatted content)"""
    try:
        import pdfplumber

        with pdfplumber.open(pdf_path) as pdf:
            text_content = []
            total_pages = len(pdf.pages)

            print(f"  📄 Processing with pdfplumber ({total_pages} pages)...")

            for page_num, page in enumerate(pdf.pages, 1):
                try:
                    page_text = page.extract_text()

                    if page_text and page_text.strip():
                        # Add page marker for reference
                        text_content.append(f"\n=== Page {page_num} ===\n")
                        text_content.append(page_text.strip())
                        text_content.append("\n")

                    # Progress indicator
                    if page_num % 10 == 0 or page_num == total_pages:
                        print(f"    ✓ Processed {page_num}/{total_pages} pages")

                except Exception as e:
                    print(f"    ⚠️  Could not process page {page_num}: {e}")
                    continue

            return "\n".join(text_content)

    except ImportError:
        print("  📦 pdfplumber not available, trying PyPDF2...")
        return None
    except Exception as e:
        print(f"  ❌ Error with pdfplumber: {e}")
        return None


def extract_with_pypdf2(pdf_path):
    """Fallback extraction using PyPDF2"""
    try:
        import PyPDF2

        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text_content = []
            total_pages = len(pdf_reader.pages)

            print(f"  📄 Processing with PyPDF2 ({total_pages} pages)...")

            for page_num, page in enumerate(pdf_reader.pages, 1):
                try:
                    page_text = page.extract_text()
                    if page_text.strip():
                        text_content.append(f"\n=== Page {page_num} ===\n")
                        text_content.append(page_text.strip())
                        text_content.append("\n")

                except Exception as e:
                    print(f"    ⚠️  Could not extract from page {page_num}: {e}")
                    continue

            return "\n".join(text_content)

    except Exception as e:
        print(f"  ❌ Error with PyPDF2: {e}")
        return None


def convert_pdf_to_clean_text(pdf_path, output_dir):
    """
    Convert PDF to clean text suitable for LLM processing
    """
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)

    if not pdf_path.exists():
        print(f"❌ PDF file not found: {pdf_path}")
        return False

    # Create output filename
    output_filename = pdf_path.stem + ".txt"
    output_path = output_dir / output_filename

    print(f"🔄 Converting: {pdf_path.name}")

    # Try pdfplumber first, then PyPDF2
    raw_text = extract_with_pdfplumber(pdf_path)
    if raw_text is None:
        raw_text = extract_with_pypdf2(pdf_path)

    if raw_text is None:
        print(f"❌ Failed to extract text from {pdf_path.name}")
        return False

    # Clean the extracted text
    print("  🧹 Cleaning text content...")
    cleaned_text = clean_text_content(raw_text)

    # Write to output file
    try:
        with open(output_path, "w", encoding="utf-8") as text_file:
            # Add header with metadata
            text_file.write(f"# Clean Text Extracted from: {pdf_path.name}\n")
            text_file.write(
                f"# Processed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            text_file.write(f"# Purpose: LLM-ready content for question generation\n")
            text_file.write("=" * 80 + "\n\n")
            text_file.write(cleaned_text)

        print(f"✅ Successfully created: {output_filename}")

        # Show content preview
        preview_lines = cleaned_text.split("\n")[:5]
        print("  📝 Preview:")
        for line in preview_lines:
            if line.strip():
                print(f"    {line[:80]}...")
                break

        return True

    except Exception as e:
        print(f"❌ Error writing output file: {e}")
        return False


def convert_all_pdfs():
    """
    Convert all PDFs in the pdfs directory to clean text files
    """
    # Get script directory and set up paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    pdfs_dir = project_root / "pdfs"
    output_dir = script_dir / "text"

    # Ensure output directory exists
    output_dir.mkdir(exist_ok=True)

    # Find all PDF files
    pdf_files = list(pdfs_dir.glob("*.pdf"))

    if not pdf_files:
        print(f"❌ No PDF files found in {pdfs_dir}")
        return

    print("🚀 AWS Academy PDF to Clean Text Converter")
    print("=" * 60)
    print(f"📁 Source: {pdfs_dir}")
    print(f"📁 Output: {output_dir}")
    print(f"📄 Found {len(pdf_files)} PDF file(s)")
    print("=" * 60)

    successful = 0
    failed = 0

    for pdf_file in pdf_files:
        if convert_pdf_to_clean_text(pdf_file, output_dir):
            successful += 1
        else:
            failed += 1
        print()  # Add spacing between files

    print("=" * 60)
    print(f"📊 Conversion Summary:")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📁 Output directory: {output_dir}")

    if successful > 0:
        print(f"\n🎯 Ready for LLM Question Generation!")
        print(f"   The clean text files are optimized for LLMs to:")
        print(f"   • Understand AWS concepts clearly")
        print(f"   • Generate relevant questions")
        print(f"   • Create comprehensive question banks")


def main():
    """Main function"""
    # Install required packages
    print("🔍 Checking required packages...")
    install_required_packages()

    # Convert all PDFs
    convert_all_pdfs()


if __name__ == "__main__":
    main()
