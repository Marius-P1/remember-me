<script setup>
import AgentChat from './components/AgentChat.vue'
import MemoryDashboard from './components/MemoryDashboard.vue'
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white shadow-soft py-4">
      <div class="max-w-4xl mx-auto px-4">
        <h1 class="text-2xl font-bold text-primary">Assistant AI</h1>
      </div>
    </header>
    
    <main class="h-[calc(100vh-4rem)]">
      <MemoryDashboard />
    </main>
  </div>
</template>
