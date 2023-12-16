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

async function callHaikufyRemoteProcedure(textInput) {
    return fetch(
        "http://127.0.0.1:8080/rpc",
        {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(
                {
                    jsonrpc: "2.0",
                    id: generateAPIcallId(),
                    method: "haikufy",
                    params: [textInput],
                }
            ),
        }
    );
}

async function callSaveHaikuRemoteProcedure(haikuId, variantId){
    return fetch(
        "http://127.0.0.1:8080/rpc",
        {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(
                {
                    jsonrpc: "2.0",
                    id: generateAPIcallId(),
                    method: "saveHaiku",
                    params: [haikuId, variantId],
                }
            ),
        }
    );
}

function replaceHaikuVariantButtonsWithChosenText(sectionToCleanUp, chosenText) {
    const haikuText = document.createElement("p");
    haikuText.innerText = chosenText;
    sectionToCleanUp.replaceWith(haikuText);
}

async function chooseHaikuVariant(haikuID, variant_id, sectionToCleanUp) {
    const response = await callSaveHaikuRemoteProcedure(haikuID, variant_id);
    const data = await response.json();
    replaceHaikuVariantButtonsWithChosenText(sectionToCleanUp, data.text);
}

function buildHaikuUI(haikuId, data) {
    const haiku = document.createElement("section");
    haiku.id = haikuId;

    const title = document.createElement("h2");
    title.innerText = data.haikuTitle;
    title.title = data.userPrompt;

    haiku.appendChild(title);

    const haikuVariantsContainer = document.createElement("section");
    haikuVariantsContainer.className = "haiku-variants-container";

    // create HTMLElements for each haiku variant
    const haikuVariants = data.haikuVariants.map(
        (haikuVariantFromResponse) => {
            const haikuVariant = document.createElement("button");
            haikuVariant.innerText = haikuVariantFromResponse.text;
            const variantId = haikuVariantFromResponse.id
            haikuVariant.id = variantId;
            haikuVariant.className = "haiku-variant";
            haikuVariant.addEventListener(
                "click",
                () => chooseHaikuVariant(
                    haikuId,
                    variantId,
                    haikuVariantsContainer,
                )
            );
            return haikuVariant;
        }
    );

    haikuVariants.map(variant => haikuVariantsContainer.appendChild(variant));

    haiku.appendChild(haikuVariantsContainer);
    haiku.appendChild(document.createElement("hr"))

    return haiku
}


async function sendText() {
    const textInput = document.getElementById("textInput").value;

    if (textInput) {
        const response = await callHaikufyRemoteProcedure(textInput);

        const content = await response.json();

        const [haikuId, data] = [content.haikuId, content.haikuData];

        const haiku = buildHaikuUI(haikuId, data)

        document.getElementById("userHaikus").appendChild(haiku);

        document.getElementById("textInput").value = "";
    }
}
