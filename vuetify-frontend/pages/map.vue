<template>
  <div>
    <v-card>
      <v-card-title>Interactive Map</v-card-title>
      <v-card-text>
        <div id="map" style="height: 500px; width: 100%;"></div>
      </v-card-text>
    </v-card>

    <!-- Coordinate Dialog -->
    <v-dialog v-model="dialog" max-width="400">
      <v-card>
        <v-card-title class="text-h5">
          Location Clicked
        </v-card-title>
        <v-card-text>
          <p><strong>Latitude:</strong> {{ clickedCoords.lat }}</p>
          <p><strong>Longitude:</strong> {{ clickedCoords.lng }}</p>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="dialog = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup>
import L from 'leaflet'

const dialog = ref(false)
const clickedCoords = ref({ lat: 0, lng: 0 })
let map = null

onMounted(() => {
  // Initialize the map centered on Italy (46°41′N 11°11′E)
  map = L.map('map').setView([46.683333, 11.183333], 10)

  // Add OpenStreetMap tiles
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map)

  // Add click event listener
  map.on('click', (e) => {
    clickedCoords.value = {
      lat: e.latlng.lat.toFixed(6),
      lng: e.latlng.lng.toFixed(6)
    }
    dialog.value = true
  })
})

onUnmounted(() => {
  if (map) {
    map.remove()
  }
})
</script>

<style>
/* Import Leaflet CSS */
@import 'leaflet/dist/leaflet.css';
</style>