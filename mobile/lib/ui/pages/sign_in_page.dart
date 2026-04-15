import 'package:bank_sha/shared/theme.dart';
import 'package:bank_sha/ui/widgets/buttons.dart';
import 'package:bank_sha/ui/widgets/forms.dart';
import 'package:flutter/material.dart';

class SignInPage extends StatelessWidget {
  const SignInPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 24),
        children: [
          Container(
            width: 155,
            height: 50,
            margin: const EdgeInsets.only(top: 100, bottom: 50),
            decoration: const BoxDecoration(
              image: DecorationImage(
                image: AssetImage('assets/img_logo_light.png'),
              ),
            ),
          ),
          Text(
            'Sign In &\nGrow Your Finance',
            style: blackTextStyle.copyWith(fontSize: 20, fontWeight: semiBold),
          ),
          const SizedBox(height: 50),
          Container(
            padding: const EdgeInsets.all(22),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(20),
              color: whiteColor,
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // NOTE : email
                CustomFormField(title: 'Email Address'),
                const SizedBox(height: 16),
                // NOTE : password
                CustomFormField(title: 'Password', isObscure: true),
                const SizedBox(height: 8),
                Align(
                  alignment: Alignment.centerRight,
                  child: Text('Forgot Password', style: blueTextStyle),
                ),
                const SizedBox(height: 30),
                CustomFilledButton(
                  title: 'Sign In',
                  onPress: () {
                    Navigator.pushNamedAndRemoveUntil(
                      context,
                      '/home',
                      (route) => false,
                    );
                  },
                ),
              ],
            ),
          ),
          const SizedBox(height: 30),
          CustomTextButton(
            title: 'Create new Account',
            onPress: () {
              Navigator.pushNamed(context, '/sign-up');
            },
          ),
        ],
      ),
    );
  }
}
