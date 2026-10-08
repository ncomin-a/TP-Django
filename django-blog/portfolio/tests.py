from django.test import TestCase


class PortfolioViewTests(TestCase):
    def test_index_renders_all_sections(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sobre mí")
        self.assertContains(response, "Habilidades Técnicas")
        self.assertContains(response, "Mis Proyectos")
        self.assertContains(response, "Contacto")
        self.assertContains(response, "Escape del Juicio")
