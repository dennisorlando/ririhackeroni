<template>
  <v-app>
    <v-navigation-drawer
        rail
        expand-on-hover
        permanent
    >
      <v-list>
        <v-list-item
            v-for="item in menuItems"
            :key="item.title"
            :to="item.route"
            link
        >
          <template v-slot:prepend>
            <v-icon>{{ item.icon }}</v-icon>
          </template>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-container>
        <NuxtPage />
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
const drawer = ref(false)

const menuItems = [
  { title: 'Home', route: '/', icon: 'mdi-home' },
  { title: 'Map', route: '/map', icon: 'mdi-map' },
  { title: 'Test', route: '/test', icon: 'mdi-email' },
  { title: 'Settings', route: '/wasm', icon: 'mdi-expansion-card' },
]
</script>