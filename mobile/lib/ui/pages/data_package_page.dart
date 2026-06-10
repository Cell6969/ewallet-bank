import 'package:bank_sha/shared/theme.dart';
import 'package:bank_sha/ui/widgets/buttons.dart';
import 'package:bank_sha/ui/widgets/forms.dart';
import 'package:bank_sha/ui/widgets/package_items.dart';
import 'package:flutter/material.dart';

class DataPackagePage extends StatefulWidget {
  const DataPackagePage({super.key});

  @override
  State<StatefulWidget> createState() => _DataPackagePage();
}

class _DataPackagePage extends State<DataPackagePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Paket Data')),
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 24),
        children: [
          const SizedBox(height: 30),
          Text(
            'Phone Number',
            style: blackTextStyle.copyWith(fontSize: 16, fontWeight: semiBold),
          ),
          const SizedBox(height: 14),
          CustomFormField(
            title: '+628',
            isShowTitle: false,
            // controller: phoneController,
          ),
          const SizedBox(height: 40),
          Text(
            'Select Package',
            style: blackTextStyle.copyWith(fontSize: 16, fontWeight: semiBold),
          ),
          const SizedBox(height: 14),
          Center(
            child: Wrap(
              spacing: 17,
              runSpacing: 17,
              children: [
                PackageItem(amount: 10, price: 30000, isSelected: true),
                PackageItem(amount: 10, price: 30000),
                PackageItem(amount: 10, price: 30000),
                PackageItem(amount: 10, price: 30000),
              ],
            ),
          ),

          const SizedBox(height: 135),
          CustomFilledButton(
            title: 'Continue',
            onPress: () async {
              if (await Navigator.pushNamed(context, '/pin') == true) {
                Navigator.pushNamedAndRemoveUntil(
                  context,
                  '/data-success',
                  (route) => false,
                );
              }
            },
          ),
          const SizedBox(height: 57),
        ],
      ),
    );
  }
}
