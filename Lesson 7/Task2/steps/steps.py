from behave import given, when, then
from selenium import webdriver
from pages.main_page import MainPage
from pages.search_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@given('Open target main page "{url}"')
def open_target(context, url):
    context.driver = webdriver.Chrome()
    context.main_page = MainPage(context.driver)
    context.main_page.open(url)

@when('Verify user can search')
def verify_search(context):
    context.search_page = SearchResultsPage(context.driver)
    context.search_page.search_product("Eevee Evolution Building Set")

@then('Verify product can be added to cart')
def verify_product(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.add_product_to_cart()

@then('Verify user can checkout')
def verify_checkout(context):
    context.checkout_page = CartPage(context.driver)
    context.checkout_page.view_cart_and_checkout()

@then('Verify user can see the product in the cart')
def verify_item(context):
    expected_text = "MEGA Pokémon Eevee Evolution Building Set - 470pcs"
    assert context.checkout_page.verify_item_in_checkout(expected_text), "Item is not here"
