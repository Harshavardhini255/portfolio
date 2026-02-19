const frameCount = 240; // total frames

const canvas = document.getElementById("scrollCanvas");
const context = canvas.getContext("2d");

let images = [];
let currentFrameIndex = 0;

// Resize canvas properly
function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  render();
}

window.addEventListener("resize", resizeCanvas);

// Generate frame path
const framePath = (index) =>
  `frame/ezgif-frame-${String(index).padStart(3, "0")}.jpg`;

// Preload images
function preloadImages() {
  for (let i = 1; i <= frameCount; i++) {
    const img = new Image();
    img.src = framePath(i);
    images.push(img);
  }

  images[0].onload = () => {
    resizeCanvas();
  };
}

// Render current frame
function render() {
  if (!images[currentFrameIndex]) return;

  context.clearRect(0, 0, canvas.width, canvas.height);

  const img = images[currentFrameIndex];

  // Maintain aspect ratio
  const scale = Math.max(
    canvas.width / img.width,
    canvas.height / img.height
  );

  const x = canvas.width / 2 - (img.width / 2) * scale;
  const y = canvas.height / 2 - (img.height / 2) * scale;

  context.drawImage(
    img,
    x,
    y,
    img.width * scale,
    img.height * scale
  );
}

// Scroll event
window.addEventListener("scroll", () => {
  const scrollTop = document.documentElement.scrollTop;
  const scrollHeight =
    document.documentElement.scrollHeight - window.innerHeight;

  const scrollFraction = scrollTop / scrollHeight;

  currentFrameIndex = Math.min(
    frameCount - 1,
    Math.floor(scrollFraction * frameCount)
  );

  render();
});

// Initialize
preloadImages();
