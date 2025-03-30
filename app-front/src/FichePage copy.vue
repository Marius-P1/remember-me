<template>
  <div class="relative mx-auto w-full p-8">
    <!-- Bouton retour -->
    <router-link
      to="/"
      class="absolute top-14 left-14 bg-blue-100 text-blue-800 px-4 py-2 rounded-xl shadow hover:bg-blue-200 transition"
    >
      &lt;
    </router-link>

    <div
      class="container-fixed-size bg-white bg-slate-50 p-6 font-sans flex flex-col rounded-xl"
    >
      <h1
        class="text-4xl md:text-5xl font-bold text-center mb-10 text-blue-900"
      >
        Fiche de {{ person?.name }}
      </h1>

      <div v-if="person" class="flex flex-col items-center">
        <!-- Photo principale -->
        <div
          class="w-60 h-60 rounded-full overflow-hidden mb-6 border-4 border-blue-200 shadow-lg"
        >
          <img
            :src="person.image"
            :alt="`Photo de ${person.name}`"
            class="w-full h-full object-cover"
          />
        </div>

        <h2 class="text-3xl font-bold text-blue-900 mb-2">
          {{ person.name }}
        </h2>
        <p class="text-2xl text-blue-700 mb-8">
          {{ person.relation }}
        </p>

        <!-- Souvenir texte (paragraphe) -->
        <div class="w-full mb-8">
          <h3 class="text-2xl font-bold text-blue-900 mb-2">Souvenir écrit</h3>
          <p
            class="text-lg text-gray-700 leading-relaxed bg-white p-4 rounded-xl shadow"
          >
            {{
              person.memory ||
              "C'était une personne très importante pour moi. Je garde en mémoire son sourire et sa gentillesse."
            }}
          </p>
        </div>

        <!-- Lecteur audio -->
        <div class="w-full mb-4">
          <h3 class="text-2xl font-bold text-blue-900 mb-2">Souvenir audio</h3>
          <audio controls class="w-full rounded-lg">
            <source src="../public/audio_extrait.wav" type="audio/wav" />
            Ton navigateur ne supporte pas l'élément audio.
          </audio>
        </div>
      </div>

      <!-- Personne introuvable -->
      <div v-else>
        <p class="text-center text-xl text-gray-700">
          Aucune information disponible pour cet identifiant.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import people from "./data/people.json";

const route = useRoute();
const person = ref(null);

onMounted(() => {
  const idParam = Number(route.params.id);
  person.value = people.find((p) => p.id === idParam) || null;
});
</script>

<style scoped>
/* Style custom ici si besoin */
</style>
