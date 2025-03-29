<template>
  <div class="mx-auto w-full p-8">
    <div
      class="container-fixed-size bg-white bg-slate-50 p-6 font-sans flex flex-col rounded-xl space-y-6 h-[600px]"
    >
      <div
        class="memory-app relative w-full flex-1 bg-gray-50 rounded-lg overflow-hidden shadow-lg"
      >
        <div
          class="absolute top-4 left-4 text-white text-xl z-10 hover:opacity-80 transition-opacity"
        >
          <router-link to="/album" class="text-blue-600 hover:underline">
            <h2 class="text-2xl font-bold text-gray-800">❌</h2>
          </router-link>
        </div>

        <div class="relative w-full h-full">
          <img
            src="https://images.unsplash.com/photo-1519741497674-611481863552?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
            alt="Wedding photo of smiling bride and groom"
            class="w-full h-full object-cover"
          />

          <div
            class="absolute bottom-0 left-0 right-0 bg-white bg-opacity-80 backdrop-blur-sm p-4"
          >
            <div class="flex justify-between items-center">
              <div>
                <h2 class="font-medium text-gray-800 text-4xl">
                  Votre petit-fils s'est marié… et vous y étiez !
                </h2>
                <p class="p-2 text-gray-600 text-4xl">17 juin 2022</p>
              </div>
              <div class="flex items-center space-x-6">
                <button
                  class="w-20 h-20 bg-red-500 rounded-full flex items-center justify-center"
                >
                  <span class="block w-6 h-6 bg-white rounded-sm"></span>
                </button>
                <div class="waveform flex items-center h-8 space-x-1">
                  <div
                    v-for="i in 5"
                    :key="i"
                    class="wave-bar bg-blue-500 w-1.5 h-full rounded-full"
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

<script setup>
// Aucun script pour l’instant
</script>

<style scoped>
.wave-bar {
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
