<script setup></script>
<!-- 
<template>
  <div class="mx-auto w-full p-8">
    <div
      class="container-fixed-size bg-white bg-slate-50 p-6 font-sans flex flex-col rounded-xl"
    >
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="space-y-8">
          <h2>Souvenir</h2>
        </div>
        <div>
          <router-link to="/album"> Aller à la vue Album </router-link>
        </div>
      </div>
    </div>
  </div>
</template> -->

<template>
  <div
    class="memory-app relative w-full max-w-md mx-auto bg-gray-50 rounded-lg overflow-hidden shadow-lg"
  >
    <!-- Close button -->
    <button
      class="absolute top-4 left-4 text-white text-xl z-10 hover:opacity-80 transition-opacity"
    >
      ❌
    </button>

    <!-- Wedding photo -->
    <div class="relative">
      <img
        src="https://images.unsplash.com/photo-1519741497674-611481863552?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80"
        alt="Wedding photo of smiling bride and groom"
        class="w-full h-80 object-cover"
      />

      <!-- Overlay panel -->
      <div
        class="absolute bottom-0 left-0 right-0 bg-white bg-opacity-80 backdrop-blur-sm p-4"
      >
        <div class="flex justify-between items-center">
          <!-- Text content -->
          <div>
            <h2 class="font-bold text-gray-800 text-lg">
              Your grandson's wedding… you were there!
            </h2>
            <p class="text-gray-600 text-sm">June 17, 2022</p>
          </div>

          <!-- Audio player -->
          <div class="flex items-center space-x-3">
            <button
              class="w-10 h-10 bg-red-500 rounded-full flex items-center justify-center"
            >
              <span class="block w-3 h-3 bg-white rounded-sm"></span>
            </button>

            <!-- Animated waveform -->
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
</template>

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

.wave-bar:nth-child(1) {
  animation-delay: 0s;
}
.wave-bar:nth-child(2) {
  animation-delay: 0.2s;
}
.wave-bar:nth-child(3) {
  animation-delay: 0.4s;
}
.wave-bar:nth-child(4) {
  animation-delay: 0.2s;
}
.wave-bar:nth-child(5) {
  animation-delay: 0s;
}
</style>
