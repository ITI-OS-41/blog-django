document.addEventListener("DOMContentLoaded", function () {
  const list = JSON.parse(document.querySelector("#bad-words").innerText)

  let flattened = "\\b(" + list.join("|") + ")\\b"

  let regex = new RegExp(flattened, "gi")

  document.getElementById("commects").innerHTML = document
    .getElementById("commects")
    .innerHTML.replace(regex, (originalWord, $1, $2, $3) => {
      return originalWord[0] + "*".repeat(originalWord.length - 1)
    })
})
