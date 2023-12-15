function insertText(textToInsert) {
  document.getElementById('textInput').value = textToInsert;
}

async function sendText() {
  const textInput = document.getElementById('textInput').value;

  if (textInput) {
    const response = await fetch('http://127.0.0.1:8080/haikufy', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({text: textInput}),
    });

    const data = await response.json();
    // Create a new paragraph element for each result and append it to the result div
    const haiku = document.createElement("section", );

    const title = document.createElement("h2");
    title.innerText = data.haikuTitle;
    title.title = data.userPrompt;

    const text = document.createElement('p');
    text.innerText = data.processedText;

    const breakLineAfter = document.createElement("hr")

    haiku.appendChild(title);
    haiku.appendChild(text);
    haiku.appendChild(breakLineAfter);

    document.getElementById('result').appendChild(haiku);

    // Clear the textarea for the next input
    document.getElementById('textInput').value = '';
  }
}
