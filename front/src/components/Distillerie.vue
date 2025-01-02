<template>
  <div class="mx-auto max-w-md overflow-hidden rounded-lg bg-white shadow-lg">
    <div class="p-4">
      <h1 class="text-2xl font-bold text-gray-900">
        {{ distillerie.name }}
      </h1>
      <p class="mt-2 text-gray-600">Pays: {{ distillerie.country?.data }}</p>
      <p v-if="distillerie.notes" class="mt-2 text-gray-600">
        {{ distillerie.notes }}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, type PropType } from 'vue'
import type { Distillery } from '@/types'

export default defineComponent({
  name: 'Distillerie',
  props: {
    distillerie: {
      type: Object as PropType<Distillery>,
      required: true,
    },
  },
})
</script>

<style scoped></style>
