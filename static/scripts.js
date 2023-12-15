function insertText(textToInsert) {
    document.getElementById("textInput").value = textToInsert;
}

function generateAPIcallId(length = 6) {
    let result = "";
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
        counter += 1;
    }
    return result;
}

async function callHaikufyRemoteProcedure(haiku_id, textInput) {
    return fetch(
        "http://127.0.0.1:8080/rpc",
        {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(
                {
                    jsonrpc: "2.0",
                    id: haiku_id,
                    method: "haikufy",
                    params: [textInput],
                }
            ),
        }
    );
}

function buildHaikuUI(haiku_id, data) {
    const haiku = document.createElement("section");
    haiku.id = haiku_id

    const title = document.createElement("h2");
    title.innerText = data.haikuTitle;
    title.title = data.userPrompt;

    haiku.appendChild(title);

    // create HTMLElements for each haiku variant
    const haikuVariants = data.haikuVariants.map(
        (haikuVariantFromResponse) => {
            const haikuVariant = document.createElement("button");
            haikuVariant.innerText = haikuVariantFromResponse.text;
            haikuVariant.id = haikuVariantFromResponse.id;
            haikuVariant.className = "haiku-variant";
            haikuVariant.addEventListener(
                "click",
                () => alert(haikuVariantFromResponse.id)
            );
            return haikuVariant;
        }
    );

    const haikuVariantsContainer = document.createElement("section");
    haikuVariantsContainer.className = "haiku-variants-container";
    haikuVariants.map(variant => haikuVariantsContainer.appendChild(variant));

    haiku.appendChild(haikuVariantsContainer);
    haiku.appendChild(document.createElement("hr"))

    return haiku
}


async function sendText() {
    const textInput = document.getElementById("textInput").value;

    if (textInput) {
        const haiku_id = generateAPIcallId();
        const response = await callHaikufyRemoteProcedure(haiku_id, textInput);

        const data = await response.json();

        const haiku = buildHaikuUI(haiku_id, data)

        document.getElementById("userHaikus").appendChild(haiku);

        document.getElementById("textInput").value = "";
    }
}
