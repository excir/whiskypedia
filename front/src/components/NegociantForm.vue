<template>
  <form
    @submit.prevent="handleSubmit"
    class="space-y-4 rounded bg-white p-4 shadow-md"
  >
    <div class="flex flex-col">
      <label for="name" class="mb-1 font-semibold">Nom</label>
      <input
        v-model="negociant.name"
        id="name"
        type="text"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="country" class="mb-1 font-semibold">Pays</label>
      <input
        v-model="negociant.country"
        id="country"
        type="text"
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="notes" class="mb-1 font-semibold">Notes</label>
      <textarea
        v-model="negociant.notes"
        id="notes"
        class="rounded border p-2"
      ></textarea>
    </div>
    <button
      type="submit"
      class="rounded bg-blue-500 px-4 py-2 text-white hover:bg-blue-600"
    >
      Enregistrer
    </button>
  </form>
</template>

<script lang="ts" setup>
import type { Negociant } from '@/types'
import { type PropType, defineProps, defineEmits } from 'vue'

const emit = defineEmits()

const props = defineProps({
  negociant: {
    type: Object as PropType<Negociant>,
    required: true,
  },
})

const handleSubmit = () => {
  emit('submit', props.negociant)
}
</script>
