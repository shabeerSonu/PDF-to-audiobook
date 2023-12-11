import PyPDF2
import requests
# Add yur pdf path here.
path = "YOUR PDF PATH"

with open(path, "rb") as pdf:
    pdf_reader = PyPDF2.PdfReader(pdf)
    pages = pdf_reader.pages
    texts = []
    for page in pages:
        texts.append(page.extract_text())

# Go to https://tts.verbatik.com/ and create account to get api key.

url = "https://tts.verbatik.com/api/v1/tts"

headers = {
    'Content-Type': 'application/ssml+xml',
    'Authorization': 'Bearer ADD YOUR API KEY',  # Add your api key over there.
}

for i in range(len(texts)):
    data = f"""
    <speak version='1.0'>
        <voice name='en-US-ChristopherNeural'>{texts[i]}</voice>
    </speak>
    """

    response = requests.post(url, headers=headers, data=data)

    # Ensure the request was successful
    response.raise_for_status()

    # Write the response to an output file
    with open(f"page{i+1}.mp3", 'wb') as f:
        f.write(response.content)
