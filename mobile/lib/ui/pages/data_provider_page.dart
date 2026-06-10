import 'package:bank_sha/shared/theme.dart';
import 'package:bank_sha/shared/utils.dart';
import 'package:bank_sha/ui/widgets/buttons.dart';
import 'package:bank_sha/ui/widgets/data_provider_items.dart';
import 'package:flutter/material.dart';

class DataProviderPage extends StatefulWidget {
  const DataProviderPage({super.key});

  @override
  State<StatefulWidget> createState() => _DataProviderPageState();
}

class _DataProviderPageState extends State<DataProviderPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Beli Data')),
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 24),
        children: [
          const SizedBox(height: 30),
          Text(
            'From Wallet',
            style: blackTextStyle.copyWith(fontSize: 16, fontWeight: semiBold),
          ),
          const SizedBox(height: 10),
          Row(
            children: [
              Image.asset('assets/img_wallet.png', width: 80),
              const SizedBox(width: 16),
              Column(
                children: [
                  Text(
                    '1234 5678 9872',
                    style: blackTextStyle.copyWith(
                      fontSize: 16,
                      fontWeight: medium,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    'Balance: ${formatCurrency(50000000)}',
                    style: greyTextStyle.copyWith(fontSize: 12),
                  ),
                ],
              ),
            ],
          ),
          const SizedBox(height: 40),
          Text(
            'Select Provider',
            style: blackTextStyle.copyWith(fontSize: 16, fontWeight: semiBold),
          ),
          const SizedBox(height: 14),
          DataProviderItem(
            name: 'Telkomsel',
            status: 'available',
            url: 'assets/img_provider_telkomsel.png',
            isSelected: true,
          ),
          DataProviderItem(
            name: 'Singtel',
            status: 'available',
            url: 'assets/img_provider_singtel.png',
          ),
          DataProviderItem(
            name: 'Indosat',
            status: 'available',
            url: 'assets/img_provider_indosat.png',
          ),
          const SizedBox(height: 135),
          CustomFilledButton(title: 'Continue', onPress: (){
            Navigator.pushNamed(context, '/data-package');
          },),
          const SizedBox(height: 57),
        ],
      ),
    );
  }
}
