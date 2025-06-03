<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Malay Translator</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div class="container">
    <h1>🇲🇾 Malay Translator</h1>
    <textarea id="inputText" placeholder="Taip dalam Bahasa Melayu..."></textarea>
    <select id="targetLang">
      <option value="en">English</option>
      <option value="fr">French</option>
      <option value="zh">Chinese</option>
      <option value="es">Spanish</option>
      <option value="ja">Japanese</option>
    </select>
    <button onclick="translateText()">Translate</button>
    <div id="result"></div>
  </div>

  <script>
    async function translateText() {
      const text = document.getElementById("inputText").value;
      const targetLang = document.getElementById("targetLang").value;

      const response = await fetch("https://libretranslate.de/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          q: text,
          source: "ms",
          target: targetLang,
          format: "text"
        })
      });

      const data = await response.json();
      document.getElementById("result").innerText = "Translation: " + data.translatedText;
    }
  </script>
</body>
</html>




