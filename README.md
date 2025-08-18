# AWS Modules PDF

A comprehensive collection of multiple-choice questions (MCQs) for AWS Academy Cloud Foundations modules.


Questions are organized by difficulty and type:
- `[E]` = Easy, `[M]` = Medium, `[H]` = Hard  
- `[SA]` = Single Answer, `[MS]` = Multi-Select

Each question includes answers and explanations for comprehensive study preparation.

# 📘 How to Download Protected PDFs from AWS Academy (Content Controller)

Sometimes AWS Academy course materials (like **Student Guides**) open inside a web viewer and don’t provide a download button. If you try to copy the PDF link directly, you’ll see this error:

> **Content can only be accessed by the launch process. Please launch your course again.**

This happens because the PDF requires **authenticated session cookies** from Canvas/LTI launch.
Here’s how you can still download the PDF for **personal offline use**.

---

## ✅ Step 1: Open Developer Tools

1. Open your course in Canvas → launch the **Student Guide**.
2. Press:

   * `Ctrl + Shift + I` (Windows/Linux) or
   * `Cmd + Option + I` (Mac)
     to open **Developer Tools**.
3. Go to the **Network** tab.

---

## ✅ Step 2: Find the PDF Request

1. In the filter bar, type **`.pdf`**.
2. Click the “Load Student Guide” button in Canvas.
3. A request ending in `.pdf` will appear (something like):

```
https://emergingtalent.contentcontroller.com/vault/.../100-ACCLFO-20-EN-M01SG.pdf
```

---

## ✅ Step 3: Copy Request as cURL

1. Right-click the PDF request.
2. Select:
   **Copy → Copy as cURL (bash)**

This copies the full request, including authentication headers.

---

## ✅ Step 4: Download with cURL

1. Open a terminal (Mac/Linux) or Git Bash (Windows).
2. Paste the copied command.
   It will look something like this:

```bash
curl 'https://emergingtalent.contentcontroller.com/vault/623cc35f.../100-ACCLFO-20-EN-M01SG.pdf' \
  -H 'authority: emergingtalent.contentcontroller.com' \
  -H 'cookie: sessionid=xyz; other_cookies=abc' \
  --compressed -o student-guide.pdf
```

3. Hit **Enter**.
4. The PDF will download to your current folder as `student-guide.pdf`.

---

## ✅ Step 5: Enjoy Offline Access

Now you have the official AWS Academy PDF saved locally for offline study. 🎉

---

### ⚠️ Important Notes

* This method is only for **personal educational use**.
* Do not share the PDFs publicly — AWS Academy materials are copyrighted.
* If your session expires, repeat the steps to generate a new cURL command.
