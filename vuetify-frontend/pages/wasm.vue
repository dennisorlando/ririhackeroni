<template>
  <div id="app">
    <h1>Bevy WASM Frontend</h1>
    <div ref="wasmCanvasContainer"></div>
  </div>
</template>

<script>
export default {
  name: "BevyWasmPage",

  mounted() {
    // Dynamically load the JS file that initializes the WASM module
    import("../../bevy-wasm-frontend/out/bevy-wasm-frontend.js")
        .then((wasmModule) => {
          // Assuming the default export initializes the app
          if (wasmModule && typeof wasmModule.default === "function") {
            wasmModule.default().then(() => {
              console.log("Bevy WASM module initialized.");
            });
          } else {
            console.warn("Could not initialize the WASM module.");
          }
        })
        .catch((error) => {
          console.error("Failed to load WASM module:", error);
        });
  },
};
</script>