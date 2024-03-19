package com.dissan;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
public class LoginGraphicsController {

    @GetMapping("/sign_up")
    public String signUp(){
        return "sign_up";
    }

    @GetMapping("/sign_in")
    public String signIn(){
        return "sign_in";
    }

    @PostMapping("/signInConfirm")
    public String singInConfirm(@RequestParam("username") String username, @RequestParam("password") String password) {
        System.out.println("{\nUsername: " + username + "\nPassword: " + password + "\n}");
        return "redirect:/sign_in";
    }

    @PostMapping("/signUpConfirm")
    public String signUpConfirm(@RequestParam("username") String username, @RequestParam("password") String password) {
        System.out.println("{\nUsername: " + username + "\nPassword: " + password + "\n}");
        return "redirect:/sign_in";
    }
}
