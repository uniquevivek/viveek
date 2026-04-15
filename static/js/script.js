// loader js
  const loader = document.getElementById("loader");
  const progressEl = document.getElementById("progress");

  // Handle back/forward cache
  window.addEventListener("pageshow", function (event) {
    if (event.persisted) {
      loader.style.display = "none";
      document.body.classList.remove("loading");
    }
  });

  // First visit check
  if (!sessionStorage.getItem("loaderShown")) {
    loader.classList.remove("hidden");
    document.body.classList.add("loading");

    let progress = 0;
    const interval = setInterval(() => {
      progress++;
      progressEl.textContent = progress + "%";

      if (progress >= 100) {
        clearInterval(interval);

        loader.style.transition = "opacity 0.7s ease";
        loader.style.opacity = "0";

        setTimeout(() => {
          loader.style.display = "none";
          document.body.classList.remove("loading");
          sessionStorage.setItem("loaderShown", "true");
        }, 700);
      }
    }, 25);
  } else {
    // Already visited → ensure hidden
    loader.style.display = "none";
  }
