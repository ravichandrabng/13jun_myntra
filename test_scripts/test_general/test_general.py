import allure
import pytest

from source.pages import page_manager as pm


class TestGeneral:

    @pytest.mark.general
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("TC001 - Verify that links under all the products across different categories are not broken. ")
    def test_tc_001_verify_the_links_are_not_broken(self, request):
        dashboard = pm.get_dashboard_page(request.node.driver)

        assert dashboard.verify_the_links_under_men_bar_not_broken(), \
            "Some of the links under menu bar is broken"

    @pytest.mark.general
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("TC002 - Verify that all the links are redirecting to correct product pages and none of the "
                        "links are broken.")
    def test_tc_002_verify_correct_product_pages_and_links_are_not_broken(self, request):
        dashboard = pm.get_dashboard_page(request.node.driver)

        dashboard.enter_product_name_in_search_box("Mens Tshirts")
        # Write a code to verify the right products are disaplying after the search

    @pytest.mark.general
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("TC003 - Verify that the company logo is clearly visible.")
    def test_tc_003_company_logo_visible(self, request):
        dashboard = pm.get_dashboard_page(request.node.driver)

        assert dashboard.company_logo_displayed(), "Company logo is not visible. "
        assert dashboard.company_logo_broken(), "Company logo is visible, but company logo image is broken"
        print("Company logo visible and it is not broken. (Valid Image)")
