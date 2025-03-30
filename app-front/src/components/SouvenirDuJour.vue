<template>
  <section class="relative h-full rounded-xl overflow-hidden shadow-md">
    <img
      :src="currentMemory.image"
      :alt="currentMemory.title"
      class="h-full w-full object-cover"
    />
    <div
      class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/50 to-transparent flex flex-col justify-end p-6"
    >
      <p class="text-sm text-white mb-1">Souvenir du jour</p>
      <h3 class="text-xl font-semibold text-white mb-1">
        {{ currentMemory.description }}
      </h3>
      <p class="text-sm text-white opacity-80">{{ currentMemory.date }}</p>
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
      image:
        "https://upload.wikimedia.org/wikipedia/commons/e/ef/Photographie-mariage.jpg",
      description: "Le mariage de ton petit-fils... tu y étais !",
      date: "17 juin 2022",
    });

    return {
      currentMemory,
    };
  },
};
</script>
