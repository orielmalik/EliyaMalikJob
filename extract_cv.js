const mammoth = require("mammoth");
const fs = require("fs");

async function extractText(filePath) {
    try {
        const result = await mammoth.extractRawText({ path: filePath });
        console.log(result.value);
    } catch (error) {
        console.error("Error extracting text:", error);
    }
}

const filePath = process.argv[2];
if (!filePath) {
    console.log("Usage: node extract_cv.js <file_path>");
} else {
    extractText(filePath);
}
