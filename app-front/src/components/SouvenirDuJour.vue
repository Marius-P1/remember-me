<template>
  <section class="rounded-xl border border-slate-200 bg-slate-50 p-6 shadow-sm">
    <h2 class="mb-4 flex items-center text-2xl font-bold text-slate-800">
      <heart-icon class="mr-2 h-7 w-7" />
      Souvenir du jour
    </h2>

    <div class="rounded-lg bg-white p-6 shadow-sm">
      <div v-if="currentMemory.image" class="mb-4 overflow-hidden rounded-lg">
        <img
          :src="currentMemory.image"
          :alt="currentMemory.title"
          class="h-64 w-full object-cover"
        />
      </div>

      <h3 class="mb-2 text-xl font-semibold text-slate-800">
        {{ currentMemory.title }}
      </h3>
      <p class="text-lg text-slate-600">
        {{ currentMemory.description }}
      </p>
    </div>
  </section>
</template>

<script>
import { ref } from "vue";
import { Heart as HeartIcon } from "lucide-vue-next";

export default {
  name: "SouvenirDuJour",
  components: {
    HeartIcon,
  },
  setup() {
    // On remplace l'URL de l'image par celle souhaitée
    const currentMemory = ref({
      title: "Mariage de mon petit fils - Été 2019",
      image:
        "https://upload.wikimedia.org/wikipedia/commons/e/ef/Photographie-mariage.jpg",
      description: "Un merveilleux souvenir de ce jour inoubliable.",
    });

    const showMemoryEditor = ref(false);
    // On initialise editingMemory avec le contenu de currentMemory
    const editingMemory = ref({ ...currentMemory.value });

    const saveMemory = () => {
      currentMemory.value = { ...editingMemory.value };
      showMemoryEditor.value = false;
    };

    return {
      currentMemory,
      showMemoryEditor,
      editingMemory,
      saveMemory,
    };
  },
};
</script>
