class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    frontend_skills = ["JavaScript", "HTML", "CSS"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        for skill in self.frontend_skills:
            self.learn_skill(skill)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    backend_skills = ["Python", "SQL", "Django"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        for skill in self.backend_skills:
            self.learn_skill(skill)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    android_skills = ["Java", "Android studio"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        for skill in self.android_skills:
            self.learn_skill(skill)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper,
                         BackendDeveloper,
                         ):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        super().create_powerful_api()
        super().create_awesome_web_page()


if __name__ == "__main__":
    full_stack_dev = FullStackDeveloper("Tom")
    print(full_stack_dev.skills)
    full_stack_dev.create_web_application()
