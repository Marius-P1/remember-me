<template>
  <section class="relative h-full rounded-xl overflow-hidden shadow-md">
    <img
      :src="currentMemory.image"
      :alt="currentMemory.title"
      class="h-full w-full object-cover"
    />
    <div
      class="absolute bottom-0 left-0 right-0 h-40 bg-gradient-to-t from-black/80 via-black/50 to-transparent flex flex-col justify-end p-6"
    >
      <h3 class="text-3xl font-semibold text-white mb-2">
        {{ currentMemory.description }}
      </h3>
      <p class="text-2xl text-white opacity-80">{{ currentMemory.date }}</p>
    </div>
  </section>
</template>

<script>
import { ref } from "vue";

export default {
  name: "SouvenirDuJour",
  setup() {
    const currentMemory = ref({
      title: "Le mariage de ton petit-fils",
      image: "photo_mariage_Thibault.png",
      description: "Le mariage de ton petit-fils... tu y étais !",
      date: "17 juin 2022",
    });

    return {
      currentMemory,
    };
  },
};
</script>
