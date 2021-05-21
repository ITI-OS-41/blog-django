document.addEventListener("DOMContentLoaded", function () {
  const list = ["bad", "test"]
  let flattened = "\\b(" + list.join("|") + ")\\b"

  let regex = new RegExp(flattened, "gi")

  document.body.innerHTML = document.body.innerHTML.replace(
    regex,
    ($0, $1, $2, $3) => {
      return "*".repeat($1.length + 1)
    },
  )
})
