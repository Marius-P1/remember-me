<template>
  <div class="mx-auto w-full p-8">
    <!-- Bouton retour -->

    <div
      class="relative container-fixed-size bg-white bg-slate-50 p-6 font-sans flex flex-col rounded-xl"
    >
      <router-link
        to="/"
        class="absolute top-8 left-8 bg-blue-100 text-blue-800 px-4 py-2 rounded-xl shadow hover:bg-blue-200 transition"
      >
        &lt;
      </router-link>

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

        <!-- Souvenir texte (paragraphe) -->
        <div class="w-full mb-8">
          <h3 class="text-2xl font-bold text-blue-900 mb-2">
            Souvenir de {{ person.name }}, {{ person.relation }}
          </h3>
          <p
            class="text-lg text-gray-700 leading-relaxed bg-white p-4 rounded-xl shadow"
          >
            {{
              person.description ||
              "C'était une personne très importante pour moi. Je garde en mémoire son sourire et sa gentillesse."
            }}
          </p>
        </div>

        <!-- Lecteur audio amélioré -->
        <div class="flex items-center space-x-6">
          <!-- Bouton PLAY -->
          <button
            v-if="!isPlaying"
            @click="playAudio"
            class="w-20 h-20 bg-green-500 rounded-full flex items-center justify-center shadow-lg text-white text-5xl font-bold"
          >
            <span class="transform rotate-90 block leading-none">▲</span>
          </button>
          <!-- Bouton STOP -->
          <button
            v-else
            @click="stopAudio"
            class="w-20 h-20 bg-red-500 rounded-full flex items-center justify-center shadow-lg text-white text-4xl font-bold"
          >
            &#9632;
          </button>

          <!-- Audio tag -->
          <audio
            ref="audioRef"
            :src="person.audiodescription || '../public/audio_extrait.wav'"
            preload="auto"
          />

          <!-- Animation bars -->
          <div class="waveform flex items-center h-8 space-x-1">
            <div
              v-for="i in 5"
              :key="i"
              class="wave-bar bg-blue-500 w-1.5 h-full rounded-full"
              :class="{ active: isPlaying }"
              :style="`animation-delay: ${i * 0.1}s`"
            ></div>
          </div>
        </div>
      </div>

      <!-- Personne introuvable -->
      <div v-else>
        <p class="text-center text-xl text-gray-700">
          Aucune information disponible pour cette personne.
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
const isPlaying = ref(false);
const audioRef = ref(null);

onMounted(() => {
  const idParam = Number(route.params.id);
  person.value = people.find((p) => p.id === idParam) || null;
});

const playAudio = () => {
  if (audioRef.value) {
    audioRef.value.play();
    isPlaying.value = true;
  }
};

const stopAudio = () => {
  if (audioRef.value) {
    audioRef.value.pause();
    audioRef.value.currentTime = 0;
    isPlaying.value = false;
  }
};
</script>

<style scoped>
.wave-bar {
  height: 20%;
  transition: height 0.3s ease;
}

.wave-bar.active {
  animation: wave 1.2s ease-in-out infinite;
  transform-origin: bottom;
}

@keyframes wave {
  0%,
  100% {
    height: 20%;
  }
  50% {
    height: 100%;
  }
}
</style>
