<!-- filepath: /Users/adrienschricke/Projects/whiskypedia/front/whiskypedia/src/components/NavBar.vue -->
<template>
    <nav class="bg-gray-800 p-4">
      <div class="container mx-auto flex justify-between items-center">
        <div class="text-white text-lg font-bold">Whiskypedia</div>
        <div class="flex space-x-4">
          <router-link to="/" class="text-gray-300 hover:text-white">Whisky</router-link>
          <router-link to="/distillerie" class="text-gray-300 hover:text-white">Distillerie</router-link>
          <router-link to="/negociant" class="text-gray-300 hover:text-white">Négociant</router-link>
        </div>
      </div>
    </nav>
  </template>
  
  <script lang="ts" setup>
  </script>