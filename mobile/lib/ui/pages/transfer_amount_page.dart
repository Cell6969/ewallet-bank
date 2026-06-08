import 'package:bank_sha/shared/theme.dart';
import 'package:bank_sha/ui/widgets/buttons.dart';
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:url_launcher/url_launcher.dart';

class TransferAmountPage extends StatefulWidget {
  const TransferAmountPage({super.key});

  @override
  State<TransferAmountPage> createState() => _TransferAmountPage();
}

class _TransferAmountPage extends State<TransferAmountPage> {
  final TextEditingController amountController = TextEditingController(text: '0');
  String pin = '123456';

  @override
  void initState() {
    super.initState();

    amountController.addListener(() {
      final text = amountController.text;
      final cleanText = text.replaceAll(RegExp(r'[^0-9]'), '');

      if (cleanText.isEmpty) return;

      final formatted = NumberFormat.currency(
        locale: 'id',
        decimalDigits: 0,
        symbol: '',
      ).format(int.parse(cleanText));

      if (formatted != text) {
        amountController.value = amountController.value.copyWith(
          text: formatted,
        );
      }
    });
  }

  addAmount(String number) {
    if (amountController.text == '0') {
      amountController.text = '';
    }

    setState(() {
      amountController.text = amountController.text + number;
    });
  }

  deleteAmount() {
    if (amountController.text.isNotEmpty) {
      setState(() {
        amountController.text = amountController.text.substring(
          0,
          amountController.text.length - 1,
        );

        if (amountController.text == '') {
          amountController.text = '0';
        }
      });
    }
  }

  @override
  void dispose() {
    amountController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: darkBackgroundColor,
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 58),
        children: [
          const SizedBox(height: 60),
          Center(
            child: Text(
              'Total Amount',
              style: whiteTextStyle.copyWith(
                fontSize: 20,
                fontWeight: semiBold,
              ),
            ),
          ),
          const SizedBox(height: 67),
          Align(
            child: SizedBox(
              width: 200,
              child: TextFormField(
                controller: amountController,
                style: whiteTextStyle.copyWith(
                  fontSize: 36,
                  fontWeight: medium,
                ),
                enabled: false,
                cursorColor: greyColor,
                decoration: InputDecoration(
                  prefixIcon: Text('Rp',style: whiteTextStyle.copyWith(
                    fontSize: 36,
                    fontWeight: medium,
                  )),
                  disabledBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: greyColor),
                  ),
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: greyColor),
                  ),
                ),
              ),
            ),
          ),
          const SizedBox(height: 66),
          Wrap(
            spacing: 40,
            runSpacing: 40,
            children: [
              CustomPinButton(title: '1', onTap: () => addAmount('1')),
              CustomPinButton(title: '2', onTap: () => addAmount('2')),
              CustomPinButton(title: '3', onTap: () => addAmount('3')),
              CustomPinButton(title: '4', onTap: () => addAmount('4')),
              CustomPinButton(title: '5', onTap: () => addAmount('5')),
              CustomPinButton(title: '6', onTap: () => addAmount('6')),
              CustomPinButton(title: '7', onTap: () => addAmount('7')),
              CustomPinButton(title: '8', onTap: () => addAmount('8')),
              CustomPinButton(title: '9', onTap: () => addAmount('9')),
              const SizedBox(width: 60),
              CustomPinButton(title: '0', onTap: () => addAmount('0')),
              GestureDetector(
                onTap: () {
                  deleteAmount();
                },
                child: Container(
                  width: 60,
                  height: 60,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: numberBackgroundColor,
                  ),
                  child: Center(
                    child: Icon(Icons.arrow_back, color: whiteColor),
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 50,),
          CustomFilledButton(title: 'Continue', onPress: () async {
            if (await Navigator.pushNamed(context, '/pin') == true) {
              if (context.mounted) {
                Navigator.pushNamedAndRemoveUntil(context, '/transfer-success', (route) => false);
              }
            }
          },),
          const SizedBox(height: 25,),
          CustomTextButton(title: 'Term & Condition', onPress: (){},),
          const SizedBox(height: 40,)
        ],
      ),
    );
  }
}
