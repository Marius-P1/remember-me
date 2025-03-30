<template>
  <div class="mx-auto w-full p-8">
    <!-- Bouton retour -->
    <div
      class="relative container-fixed-size bg-white bg-slate-50 p-6 font-sans flex flex-col rounded-xl"
    >
      <router-link
        to="/"
        class="absolute top-4 left-4 z-20 bg-[#0035EB] rounded-full p-4 shadow-lg hover:bg-[#002bd1] transition"
        aria-label="Retour"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-8 w-8 text-white"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M15 19l-7-7 7-7"
          />
        </svg>
      </router-link>

      <h1
        class="text-4xl md:text-5xl font-bold text-center mb-10 text-blue-900"
      >
        {{ person?.name }}
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

        <!-- Souvenir texte -->
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

        <!-- Lecteur audio avec boutons stylisés -->
        <div class="flex items-center space-x-6">
          <!-- Bouton PLAY -->
          <button
            v-if="!isPlaying"
            @click="playAudio"
            class="w-20 h-20 bg-green-500/60 rounded-xl flex items-center justify-center shadow-lg"
          >
            <span
              class="text-white text-5xl font-bold transform rotate-90 opacity-100"
            >
              ▲
            </span>
          </button>

          <!-- Bouton STOP -->
          <button
            v-else
            @click="stopAudio"
            class="w-20 h-20 bg-red-500/40 rounded-xl flex items-center justify-center shadow-lg"
          >
            <span class="text-white text-4xl font-bold opacity-100">
              &#9632;
            </span>
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
