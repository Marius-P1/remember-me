<template>
  <header class="mb-8 text-center">
    <div class="text-5xl font-bold text-slate-800">{{ currentTime }}</div>
    <div class="mt-2 text-3xl font-medium text-slate-600">
      {{ currentDate }}
    </div>
  </header>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "HeureDate",
  setup() {
    const currentTime = ref("");
    const currentDate = ref("");

    const updateDateTime = () => {
      const now = new Date();

      // Format de l'heure (HH:MM)
      currentTime.value = now.toLocaleTimeString("fr-FR", {
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
      });

      // Format de la date (Jour DD Mois YYYY)
      currentDate.value = now.toLocaleDateString("fr-FR", {
        weekday: "long",
        day: "numeric",
        month: "long",
        year: "numeric",
      });
    };

    onMounted(() => {
      updateDateTime();
      // Mise à jour chaque minute
      setInterval(updateDateTime, 60000);
    });

    return {
      currentTime,
      currentDate,
    };
  },
};
</script>
