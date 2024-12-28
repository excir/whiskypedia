<template>
  <div class="mx-auto max-w-md overflow-hidden rounded-lg bg-white shadow-lg">
    <div
      class="h-56 bg-cover bg-center p-4"
      :style="{ backgroundImage: `url(${whisky.photo})` }"
    ></div>
    <div class="p-4">
      <h1 class="text-2xl font-bold text-gray-900">{{ whisky.name }}</h1>
      <p class="mt-2 text-gray-600">{{ whisky.whisky_type }}</p>
      <p class="mt-2 text-gray-600">
        Distillery: {{ whisky.distillery?.name }}
      </p>
      <p class="mt-2 text-gray-600">
        Alcohol: {{ whisky.alcohol_percentage }}%
      </p>
      <p class="mt-2 text-gray-600">Price: ${{ whisky.price }}</p>
      <p class="mt-2 text-gray-600" v-if="whisky.is_peated">Peated</p>
      <p class="mt-2 text-gray-600" v-if="whisky.nose">
        Nose: {{ whisky.nose }}
      </p>
      <p class="mt-2 text-gray-600" v-if="whisky.appearance">
        Appearance: {{ whisky.appearance }}
      </p>
      <p class="mt-2 text-gray-600" v-if="whisky.palate">
        Palate: {{ whisky.palate }}
      </p>
      <p class="mt-2 text-gray-600" v-if="whisky.finish">
        Finish: {{ whisky.finish }}
      </p>
      <p class="mt-2 text-gray-600" v-if="averageRating !== null">
        Note moyenne:
        <v-rating
          half-increments
          :length="5"
          :size="28"
          color="warning"
          active-color="warning"
          :model-value="averageRating / 2"
          readonly
        />
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, type PropType, computed } from 'vue'
import type { Whisky } from '@/types'

export default defineComponent({
  name: 'Whisky',
  props: {
    whisky: {
      type: Object as PropType<Whisky>,
      required: true,
    },
  },
  setup(props) {
    const averageRating = computed(() => {
      if (!props.whisky.tastings || props.whisky.tastings.length === 0) {
        return null
      }
      const total = props.whisky.tastings.reduce(
        (sum, tasting) => sum + tasting.rating,
        0
      )
      return total / props.whisky.tastings.length
    })

    return {
      averageRating,
    }
  },
})
</script>

<style scoped></style>
