<template>
  <section class="rounded-xl border border-slate-200 bg-slate-50 p-6 shadow-sm">
    <h2 class="mb-4 flex items-center text-2xl font-bold text-slate-800">
      <calendar-icon class="mr-2 h-7 w-7" />
      Agenda
    </h2>

    <!-- Section : Aujourd'hui -->
    <div class="mb-8">
      <h3 class="mb-4 text-xl font-semibold text-gray-900">Aujourd'hui</h3>
      <div
        v-for="(event, index) in todayEvents"
        :key="index"
        class="mb-4 rounded-lg border border-slate-200 bg-white p-4 shadow-sm"
      >
        <div class="flex items-start">
          <!-- Icône d'horloge avec heure à côté -->
          <div class="mr-3 flex items-center">
            <clock-icon class="h-6 w-6 text-gray-800 mr-2" />
            <span class="text-lg font-medium text-gray-800">{{
              event.time
            }}</span>
          </div>

          <!-- Texte & image -->
          <div class="flex-1">
            <div class="mb-1 text-xl font-medium text-slate-800">
              {{ event.title }}
            </div>
            <div class="text-base text-slate-600">
              {{ event.description }}
            </div>

            <div v-if="event.image" class="mt-2">
              <img
                :src="event.image"
                alt="Personne"
                class="h-12 w-12 rounded-full object-cover"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section : Demain -->
    <div>
      <h3 class="mb-4 text-xl font-semibold text-gray-900">Demain</h3>
      <div
        v-for="(event, index) in tomorrowEvents"
        :key="index"
        class="mb-4 rounded-lg border border-slate-200 bg-white p-4 shadow-sm"
      >
        <div class="flex items-start">
          <!-- Icône d'horloge avec heure à côté -->
          <div class="mr-3 flex items-center">
            <clock-icon class="h-6 w-6 text-gray-800 mr-2" />
            <span class="text-lg font-medium text-gray-800">{{
              event.time
            }}</span>
          </div>

          <!-- Texte & image -->
          <div class="flex-1">
            <div class="mb-1 text-xl font-medium text-slate-800">
              {{ event.title }}
            </div>
            <div class="text-base text-slate-600">
              {{ event.description }}
            </div>

            <div v-if="event.image" class="mt-2">
              <img
                :src="event.image"
                alt="Personne"
                class="h-12 w-12 rounded-full object-cover"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, computed } from "vue";
import { Calendar as CalendarIcon, Clock as ClockIcon } from "lucide-vue-next";

export default {
  name: "AgendaExample",
  components: {
    CalendarIcon,
    ClockIcon,
  },
  setup() {
    // Petit utilitaire pour vérifier si deux dates sont le même jour
    const isSameDay = (d1, d2) => {
      return (
        d1.getFullYear() === d2.getFullYear() &&
        d1.getMonth() === d2.getMonth() &&
        d1.getDate() === d2.getDate()
      );
    };

    // Détermine "aujourd'hui" et "demain"
    const today = new Date();
    const tomorrow = new Date(today);
    tomorrow.setDate(tomorrow.getDate() + 1);

    // Données d'exemple
    const events = ref([
      {
        date: new Date().toISOString(),
        time: "9h00",
        title: "Infirmière",
        description: "Anaïs vient faire les soins",
        color: "green",
        image: "https://randomuser.me/api/portraits/women/28.jpg",
      },

      {
        date: new Date().toISOString(),
        time: "16h30",
        title: "Rdv Ophtalmologue",
        description: "Accompagner Fred, petit-fils",
        color: "green",
        image: "https://randomuser.me/api/portraits/men/32.jpg",
      },
      {
        date: new Date(
          new Date().setDate(new Date().getDate() + 1)
        ).toISOString(),
        time: "13h30",
        title: "Visite",
        description: "Carole, ta fille, viendra te rendre visite",
        color: "green",
        image: "https://randomuser.me/api/portraits/women/35.jpg",
      },
    ]);

    const todayEvents = computed(() =>
      events.value.filter((e) => isSameDay(new Date(e.date), today))
    );
    const tomorrowEvents = computed(() =>
      events.value.filter((e) => isSameDay(new Date(e.date), tomorrow))
    );

    const getColorClass = (color) => {
      switch (color) {
        case "green":
          return "bg-green-100 text-green-600";
        case "blue":
          return "bg-blue-100 text-blue-600";
        case "red":
          return "bg-red-100 text-red-600";
        default:
          return "bg-gray-100 text-gray-600";
      }
    };

    return {
      events,
      todayEvents,
      tomorrowEvents,
      getColorClass,
    };
  },
};
</script>

<style scoped>

</style>
