<!-- filepath: /Users/adrienschricke/Projects/whiskypedia/front/whiskypedia/src/components/WhiskyForm.vue -->
<template>
  <form @submit.prevent="handleSubmit">
    <div>
      <label for="name">Nom</label>
      <input v-model="whisky.name" id="name" type="text" required />
    </div>
    <div>
      <label for="distillery_id">Distillerie</label>
      <input
        v-model="whisky.distillery_id"
        id="distillery_id"
        type="text"
        required
      />
    </div>
    <div>
      <label for="negotiant_id">Négociant</label>
      <input
        v-model="whisky.negotiant_id"
        id="negotiant_id"
        type="text"
        required
      />
    </div>
    <div>
      <label for="alcohol_percentage">Pourcentage d'alcool</label>
      <input
        v-model="whisky.alcohol_percentage"
        id="alcohol_percentage"
        type="number"
        required
      />
    </div>
    <div>
      <label for="whisky_type">Type de whisky</label>
      <input
        v-model="whisky.whisky_type"
        id="whisky_type"
        type="text"
        required
      />
    </div>
    <div>
      <label for="bottle_size_cl">Taille de la bouteille (cl)</label>
      <input
        v-model="whisky.bottle_size_cl"
        id="bottle_size_cl"
        type="number"
        required
      />
    </div>
    <div>
      <label for="price">Prix</label>
      <input v-model="whisky.price" id="price" type="number" required />
    </div>
    <div>
      <label for="is_peated">Tourbé</label>
      <input v-model="whisky.is_peated" id="is_peated" type="checkbox" />
    </div>
    <div>
      <label for="nose">Nez</label>
      <textarea v-model="whisky.nose" id="nose"></textarea>
    </div>
    <div>
      <label for="appearance">Apparence</label>
      <textarea v-model="whisky.appearance" id="appearance"></textarea>
    </div>
    <div>
      <label for="palate">Palais</label>
      <textarea v-model="whisky.palate" id="palate"></textarea>
    </div>
    <div>
      <label for="finish">Finale</label>
      <textarea v-model="whisky.finish" id="finish"></textarea>
    </div>
    <div>
      <label for="photo">Photo</label>
      <input v-model="whisky.photo" id="photo" type="text" />
    </div>
    <button type="submit">Enregistrer</button>
  </form>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { type Whisky } from '@/types'

const whisky = ref<Whisky>({
  id: '',
  name: '',
  distillery_id: '',
  negotiant_id: '',
  alcohol_percentage: 0,
  whisky_type: '',
  bottle_size_cl: 0,
  price: 0,
  is_peated: false,
  nose: '',
  appearance: '',
  palate: '',
  finish: '',
  photo: '',
})

const handleSubmit = () => {
  // Logique pour soumettre le formulaire
  console.log(whisky.value)
}
</script>
