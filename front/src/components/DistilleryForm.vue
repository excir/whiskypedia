<!-- filepath: /Users/adrienschricke/Projects/whiskypedia/front/whiskypedia/src/components/DistilleryForm.vue -->
<template>
  <form @submit.prevent="handleSubmit">
    <div>
      <label for="name">Nom</label>
      <input v-model="distillery.name" id="name" type="text" required />
    </div>
    <div>
      <label for="country">Pays</label>
      <input v-model="distillery.country" id="country" type="text" required />
    </div>
    <div>
      <label for="notes">Notes</label>
      <textarea v-model="distillery.notes" id="notes"></textarea>
    </div>
    <button type="submit">Enregistrer</button>
  </form>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { type Distillery } from '@/types'

const distillery = ref<Distillery>({
  id: '',
  name: '',
  country: '',
  notes: '',
})

const handleSubmit = () => {
  // Logique pour soumettre le formulaire
  console.log(distillery.value)
}
</script>
