<template>
  <div class="mx-auto max-w-md overflow-hidden rounded-lg bg-white shadow-lg">
    <div class="relative h-56" v-if="imageUrl">
      <img
        :src="imageUrl"
        class="absolute inset-0 h-full w-full object-contain"
      />
    </div>
    <div class="p-4">
      <h1 class="text-2xl font-bold text-gray-900">{{ whisky.name }}</h1>
      <p class="mt-2 text-gray-600">{{ whisky.whisky_type?.data }}</p>
      <p class="mt-2 text-gray-600">
        Distillerie: {{ whisky.distillery?.name }}
      </p>
      <p class="mt-2 text-gray-600">Alcool: {{ whisky.alcohol_percentage }}%</p>
      <p class="mt-2 text-gray-600">Prix: {{ whisky.price }}€</p>
      <p class="mt-2 text-gray-600">
        {{ whisky.is_peated ? 'Tourbé' : 'Non tourbé' }}
      </p>
      <p class="mt-2 text-gray-600" v-if="whisky.nose">
        Nez: {{ whisky.nose }}
      </p>
      <p class="mt-2 text-gray-600" v-if="whisky.appearance">
        Apparence: {{ whisky.appearance }}
      </p>
      <p class="mt-2 text-gray-600" v-if="whisky.palate">
        Palais: {{ whisky.palate }}
      </p>
      <p class="mt-2 text-gray-600" v-if="whisky.finish">
        Finale: {{ whisky.finish }}
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
