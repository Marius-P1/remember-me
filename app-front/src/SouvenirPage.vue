<template>
  <div class="mx-auto w-full p-8">
    <div
      class="container-fixed-size bg-white bg-slate-50 p-6 font-sans flex flex-col rounded-xl space-y-6 h-[600px]"
    >
      <div
        class="memory-app relative w-full flex-1 bg-gray-50 rounded-lg overflow-hidden shadow-lg"
      >
        <!-- Bouton retour -->
        <div
          class="absolute top-4 left-4 text-white text-xl z-10 hover:opacity-80 transition-opacity"
        >
          <router-link to="/album" class="text-blue-600 hover:underline">
            <h2 class="text-2xl font-bold text-gray-800">❌</h2>
          </router-link>
        </div>

        <!-- Image principale -->
        <div class="relative w-full h-full">
          <img :src="image" alt="Souvenir" class="w-full h-full object-cover" />

          <!-- Bandeau texte + audio -->
          <div
            class="absolute bottom-0 left-0 right-0 bg-white bg-opacity-80 backdrop-blur-sm p-4"
          >
            <div class="flex justify-between items-center">
              <div>
                <h2 class="font-medium text-gray-800 text-4xl">
                  {{ shortHistory }}
                </h2>
                <p class="p-2 text-gray-600 text-4xl">{{ date }}</p>
              </div>

              <div class="flex items-center space-x-6">
                <!-- BOUTON PLAY -->
                <button
                  v-if="!isPlaying"
                  @click="playAudio"
                  class="w-20 h-20 bg-green-500 rounded-full flex items-center justify-center shadow-lg text-white text-5xl font-bold"
                >
                  <span class="transform rotate-90 block leading-none">▲</span>
                </button>
                <!-- BOUTON STOP -->
                <button
                  v-else
                  @click="stopAudio"
                  class="w-20 h-20 bg-red-500 rounded-full flex items-center justify-center shadow-lg text-white text-4xl font-bold"
                >
                  &#9632;
                </button>

                <!-- Audio tag -->
                <audio ref="audioRef" :src="audioHistory" preload="auto" />

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
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const props = withDefaults(
  defineProps<{
    image?: string;
    shortHistory?: string;
    date?: string;
    audioHistory?: string;
  }>(),
  {
    image: "photo_mariage_Thibault.png",
    shortHistory: "Votre petit-fils s'est marié… et vous y étiez !",
    date: "17 juin 2022",
    audioHistory: "../public/audio_extrait.wav",
  }
);

const isPlaying = ref(false);
const audioRef = ref<HTMLAudioElement | null>(null);

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
