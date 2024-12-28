<template>
  <form
    @submit.prevent="handleSubmit"
    class="space-y-4 rounded bg-white p-4 shadow-md"
  >
    <div class="flex flex-col">
      <label for="name" class="mb-1 font-semibold">Nom</label>
      <input
        v-model="distillery.name"
        id="name"
        type="text"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="country" class="mb-1 font-semibold">Pays</label>
      <input
        v-model="distillery.country"
        id="country"
        type="text"
        required
        class="rounded border p-2"
      />
    </div>
    <div class="flex flex-col">
      <label for="notes" class="mb-1 font-semibold">Notes</label>
      <textarea
        v-model="distillery.notes"
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
import type { Distillery } from '@/types'
import { type PropType, defineProps } from 'vue'

const emit = defineEmits()

const props = defineProps({
  distillery: {
    type: Object as PropType<Distillery>,
    required: true,
  },
})

const handleSubmit = () => {
  emit('submit', props.distillery)
}
</script>
