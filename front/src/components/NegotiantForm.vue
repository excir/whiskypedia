<!-- filepath: /Users/adrienschricke/Projects/whiskypedia/front/whiskypedia/src/components/NegotiantForm.vue -->
<template>
  <form @submit.prevent="handleSubmit">
    <div>
      <label for="name">Nom</label>
      <input v-model="negotiant.name" id="name" type="text" required />
    </div>
    <div>
      <label for="country">Pays</label>
      <input v-model="negotiant.country" id="country" type="text" />
    </div>
    <div>
      <label for="notes">Notes</label>
      <textarea v-model="negotiant.notes" id="notes"></textarea>
    </div>
    <button type="submit">Enregistrer</button>
  </form>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { type Negotiant } from '@/types'

const negotiant = ref<Negotiant>({
  id: '',
  name: '',
  country: '',
  notes: '',
})

const handleSubmit = () => {
  // Logique pour soumettre le formulaire
  console.log(negotiant.value)
}
</script>
