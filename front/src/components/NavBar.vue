<!-- filepath: /Users/adrienschricke/Projects/whiskypedia/front/whiskypedia/src/components/NavBar.vue -->
<template>
  <nav class="bg-gray-800 p-4">
    <div class="container mx-auto flex items-center justify-between">
      <div class="text-lg font-bold text-white">Whiskypedia</div>
      <div class="flex space-x-4">
        <router-link to="/" class="text-gray-300 hover:text-white">
          Whisky
        </router-link>
        <router-link
          to="/DistillerieList"
          class="text-gray-300 hover:text-white"
        >
          Distillerie
        </router-link>
        <router-link to="/NegociantList" class="text-gray-300 hover:text-white">
          Négociant
        </router-link>
        <router-link to="/Libraries" class="text-gray-300 hover:text-white">
          Listes
        </router-link>
        <router-link to="/Backup" class="text-gray-300 hover:text-white">
          Sauvegardes
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script lang="ts" setup></script>
