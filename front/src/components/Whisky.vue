<template>
  <div class="mx-auto max-w-md overflow-hidden rounded-lg bg-white shadow-lg">
    <div v-if="imageUrl" class="relative h-56">
      <img
        :src="imageUrl"
        class="absolute inset-0 h-full w-full object-contain"
      />
    </div>
    <div class="p-4">
      <h1 class="text-2xl font-bold text-gray-900">
        {{ whisky.name }}
      </h1>
      <p class="mt-2 text-gray-600">
        {{ whisky.whisky_type?.data }}
      </p>
      <p class="mt-2 text-gray-600">
        Distillerie: {{ whisky.distillery?.name }}
      </p>
      <p class="mt-2 text-gray-600">Alcool: {{ whisky.alcohol_percentage }}%</p>
      <p class="mt-2 text-gray-600">Prix: {{ whisky.price }}€</p>
      <p class="mt-2 text-gray-600">
        {{ whisky.is_peated ? 'Tourbé' : 'Non tourbé' }}
      </p>
      <p v-if="whisky.nose" class="mt-2 text-gray-600">
        Nez: {{ whisky.nose }}
      </p>
      <p v-if="whisky.appearance" class="mt-2 text-gray-600">
        Apparence: {{ whisky.appearance }}
      </p>
      <p v-if="whisky.palate" class="mt-2 text-gray-600">
        Palais: {{ whisky.palate }}
      </p>
      <p v-if="whisky.finish" class="mt-2 text-gray-600">
        Finale: {{ whisky.finish }}
      </p>
      <p v-if="averageRating !== null" class="mt-2 text-gray-600">
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
import { useImages } from '@/stores/images'
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
    const { getImageUrl } = useImages()
    const imageUrl = computed(() => getImageUrl(props.whisky.photo))

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
      imageUrl,
    }
  },
})
</script>

<style scoped></style>
