/*
* Copyright (c) 2014 Omkar Kanase
*
* This software is provided 'as-is', without any express or implied
* warranty.  In no event will the authors be held liable for any damages
* arising from the use of this software.
* Permission is granted to anyone to use this software for any purpose,
* including commercial applications, and to alter it and redistribute it
* freely, subject to the following restrictions:
* 1. The origin of this software must not be misrepresented; you must not
* claim that you wrote the original software. If you use this software
* in a product, an acknowledgment in the product documentation would be
* appreciated but is not required.
* 2. Altered source versions must be plainly marked as such, and must not be
* misrepresented as being the original software.
* 3. This notice may not be removed or altered from any source distribution.
*/

#include "captcha.h"

Captcha::Captcha(QObject *parent) :
    QObject(parent)
{
    m_hmod1 = 0.0;
    m_hmod2 = 0.0;

    m_vmod1 = 0.0;
    m_vmod2 = 0.0;

    m_font.setStyleStrategy(QFont::ForceOutline);
    m_font.setPointSize(30);
    m_font.setBold(true);
    m_font.setLetterSpacing(QFont::PercentageSpacing, QFont::SemiCondensed);

    m_captchaImage = QImage(200, 100, QImage::Format_RGB32);
    m_deformationType = Deform_SinCurve;
    m_captchaText = "Test";

	m_textGeneration = TextGeneration_Random;
	m_fontColor = Qt::black;
	m_backColor = Qt::white;
	m_padding = 5;

	m_drawLines = true;
	m_drawEllipses = true;
	m_drawNoise = true;
	m_noiseCount = 100;
	m_lineCount = 5;
	m_ellipseCount = 1;

	m_lineWidth = 2;
	m_ellipseMinRadius = 20;
	m_ellipseMaxRadius = 40;

	m_noisePointSize = 3;

	setSinDeform(8, 10, 5, 15);
}

void Captcha::setDifficulty(int val)
{
	if (val == 0)
	{
		m_drawLines = false;
		m_drawEllipses = false;
		m_drawNoise = false;
		setSinDeform(10, 10, 5, 20);
	}
	else if (val == 1)
	{
		m_drawLines = true;
		m_lineWidth = 3;
		m_lineCount = 5;
		m_drawEllipses = false;
		m_drawNoise = false;
		setSinDeform(10, 15, 5, 20);
	}
	else if (val == 2)
	{
		m_drawLines = true;
		m_lineWidth = 2;
		m_lineCount = 5;
		m_drawEllipses = true;
		m_ellipseCount = 1;
		m_ellipseMinRadius = 20;
		m_ellipseMaxRadius = 40;
		m_drawNoise = false;
		setSinDeform(10, 15, 5, 15);
	}
	else if (val == 3)
	{
		m_drawLines = true;
		m_lineWidth = 2;
		m_lineCount = 3;
		m_drawEllipses = true;
		m_ellipseCount = 1;
		m_ellipseMinRadius = 20;
		m_ellipseMaxRadius = 40;
		m_drawNoise = true;
		m_noiseCount = 100;
		m_noisePointSize = 3;
		setSinDeform(8, 13, 5, 15);
	}
	else if (val == 4)
	{
		m_drawLines = true;
		m_lineWidth = 3;
		m_lineCount = 5;
		m_drawEllipses = true;
		m_ellipseCount = 1;
		m_ellipseMinRadius = 20;
		m_ellipseMaxRadius = 40;
		m_drawNoise = true;
		m_noiseCount = 100;
		m_noisePointSize = 3;
		setSinDeform(8, 10, 5, 10);
	}
    else
	{
		m_drawLines = true;
		m_lineWidth = 4;
		m_lineCount = 7;
		m_drawEllipses = true;
		m_ellipseCount = 1;
		m_ellipseMinRadius = 20;
		m_ellipseMaxRadius = 40;
		m_drawNoise = true;
		m_noiseCount = 200;
		m_noisePointSize = 3;
		setSinDeform(8, 10, 5, 10);
	}
}

QFont Captcha::font() const
{
    return m_font;
}

QImage Captcha::captchaImage() const
{
    return m_captchaImage;
}

Captcha::DeformType Captcha::deformationType() const
{
    return m_deformationType;
}

QString Captcha::captchaText() const
{
    return m_captchaText;
}

Captcha::TextGenerationMode Captcha::textGeneration() const
{
    return m_textGeneration;
}

const QStringList &Captcha::dictionary() const
{
    return m_dictionary;
}

QColor Captcha::fontColor() const
{
    return m_fontColor;
}

QColor Captcha::backColor() const
{
    return m_backColor;
}

bool Captcha::drawLines() const
{
    return m_drawLines;
}

bool Captcha::drawEllipses() const
{
    return m_drawEllipses;
}

bool Captcha::drawNoise() const
{
    return m_drawNoise;
}

int Captcha::noiseCount() const
{
    return m_noiseCount;
}

int Captcha::lineCount() const
{
    return m_lineCount;
}

int Captcha::ellipseCount() const
{
    return m_ellipseCount;
}

int Captcha::lineWidth() const
{
    return m_lineWidth;
}

int Captcha::ellipseMinRadius() const
{
    return m_ellipseMinRadius;
}

int Captcha::ellipseMaxRadius() const
{
    return m_ellipseMaxRadius;
}

int Captcha::noisePointSize() const
{
    return m_noisePointSize;
}

void Captcha::setFont(const QFont &arg)
{
    m_font = arg;
}

void Captcha::setDeformationType(Captcha::DeformType arg)
{
    m_deformationType = arg;
}

void Captcha::updateCaptcha()
{
	QPainterPath path;
	QFontMetrics fm(m_font);

	if (m_deformationType == Deform_SinCurve)
	{
		
		path.addText(m_vmod2 + m_padding, m_hmod2 - m_padding + fm.height(), font(), captchaText());

		qreal sinrandomness = ((qreal) qrand() / RAND_MAX) * 5.0;

		for (int i = 0; i < path.elementCount(); ++i)
		{
			const QPainterPath::Element& el = path.elementAt(i);
			qreal y = el.y + sin(el.x / m_hmod1 + sinrandomness) * m_hmod2;
			qreal x = el.x + sin(el.y / m_vmod1 + sinrandomness) * m_vmod2;
			path.setElementPositionAt(i, x, y);
		}
				
		m_captchaImage = QImage(fm.width(m_captchaText) + m_vmod2 * 2 + m_padding * 2, fm.height() + m_hmod2 * 2 + m_padding * 2, QImage::Format_RGB32);
	}

	m_captchaImage.fill(backColor());
	QPainter painter;
	painter.begin(&m_captchaImage);
	painter.setPen(Qt::NoPen);
	painter.setBrush(fontColor());
	painter.setRenderHint(QPainter::Antialiasing);
	painter.drawPath(path);

	if (m_drawLines)
	{
		painter.setPen(QPen(Qt::black, m_lineWidth));
		for (int i = 0; i < m_lineCount; i++)
		{
			int x1 = ((qreal) qrand() / RAND_MAX) * m_captchaImage.width();
			int y1 = ((qreal) qrand() / RAND_MAX) * m_captchaImage.height();
			int x2 = ((qreal) qrand() / RAND_MAX) * m_captchaImage.width();
			int y2 = ((qreal) qrand() / RAND_MAX) * m_captchaImage.height();
			painter.drawLine(x1, y1, x2, y2);
		}
		painter.setPen(Qt::NoPen);
	}

	if (m_drawEllipses)
	{
		for (int i = 0; i < m_ellipseCount; i++)
		{
			int x1 = m_ellipseMaxRadius / 2.0 + ((qreal) qrand() / RAND_MAX) * (m_captchaImage.width() - m_ellipseMaxRadius);
			int y1 = m_ellipseMaxRadius / 2.0 + ((qreal) qrand() / RAND_MAX) * (m_captchaImage.height() - m_ellipseMaxRadius);
			int rad1 = m_ellipseMinRadius + ((qreal) qrand() / RAND_MAX) * (m_ellipseMaxRadius - m_ellipseMinRadius);
			int rad2 = m_ellipseMinRadius + ((qreal) qrand() / RAND_MAX) * (m_ellipseMaxRadius - m_ellipseMinRadius);
			painter.setBrush(backColor());
			painter.setCompositionMode(QPainter::CompositionMode_Difference);
			painter.drawEllipse(QPoint(x1, y1), rad1, rad2);			
		}
	}

	if (m_drawNoise)
	{
		for (int i = 0; i < m_noiseCount; i++)
		{
			int x1 = ((qreal) qrand() / RAND_MAX) * m_captchaImage.width();
			int y1 = ((qreal) qrand() / RAND_MAX) * m_captchaImage.height();

			QColor col = QColor(((qreal) qrand() / RAND_MAX) * 255, ((qreal) qrand() / RAND_MAX) * 255, ((qreal) qrand() / RAND_MAX) * 255);

			painter.setPen(QPen(col, m_noisePointSize));
			painter.setCompositionMode(QPainter::CompositionMode_SourceOver);
			painter.drawPoint(x1, y1);
		}
	}
	painter.end();
	emit catpchaGenerated(m_captchaImage, m_captchaText);
}

void Captcha::randomize()
{
    qsrand(QTime::currentTime().msec());
}

void Captcha::setCaptchaText(QString arg)
{
    m_captchaText = arg;
}

void Captcha::setTextGeneration(Captcha::TextGenerationMode arg)
{
	if (m_textGeneration != arg) generateText(m_captchaText.size());
    m_textGeneration = arg;
}

void Captcha::setDictionary(const QStringList &arg)
{
    m_dictionary = arg;
}

void Captcha::loadDictionary(QString FileName)
{
	QFile file(FileName);
	if (!file.open(QIODevice::ReadOnly))
	{
		qCritical() << "Unable to open dictionary file";
		return;
	}

	m_dictionary.clear();
	QTextStream text(&file);
	QString str = text.readLine();
	while (str.size() > 0)
	{
		m_dictionary.append(str);
		str = text.readLine();
	}

	if (m_dictionary.size() <= 0)
	{
		qWarning() << "No data loaded from dictionary file";
	}
}

void Captcha::setFontColor(QColor arg)
{
    m_fontColor = arg;
}

void Captcha::setBackColor(QColor arg)
{
    m_backColor = arg;
}

void Captcha::setSinDeform(qreal hAmplitude, qreal hFrequency, qreal vAmplitude, qreal vFrequency)
{
	m_deformationType = Deform_SinCurve;
	m_hmod1 = hFrequency;
	m_hmod2 = hAmplitude;

	m_vmod1 = vFrequency;
    m_vmod2 = vAmplitude;
}

QPair<QString, QImage> Captcha::generateCaptcha()
{
	generateText(m_captchaText.size());
	return QPair<QString, QImage>(m_captchaText, m_captchaImage);
}

void Captcha::setDrawLines(bool arg)
{
    m_drawLines = arg;
}

void Captcha::setDrawEllipses(bool arg)
{
    m_drawEllipses = arg;
}

void Captcha::setDrawNoise(bool arg)
{
    m_drawNoise = arg;
}

void Captcha::setNoiseCount(int arg)
{
    m_noiseCount = arg;
}

void Captcha::setLineCount(int arg)
{
    m_lineCount = arg;
}

void Captcha::setEllipseCount(int arg)
{
    m_ellipseCount = arg;
}

void Captcha::setLineWidth(int arg)
{
    m_lineWidth = arg;
}

void Captcha::setEllipseMinRadius(int arg)
{
    m_ellipseMinRadius = arg;
}

void Captcha::setEllipseMaxRadius(int arg)
{
    m_ellipseMaxRadius = arg;
}

void Captcha::setNoisePointSize(int arg)
{
    m_noisePointSize = arg;
}

void Captcha::generateText(int noOfChars, bool includeNumbers, bool includeSymbols, bool allCapital)
{
 	if (noOfChars <= 0)
	{
		qWarning() << "Unable to generate text : Invalid number of characters";
		return;
	}

	QString text;

	if (m_textGeneration == TextGeneration_Random)
	{
		QVector<unsigned char> chars;
		for (int i = 0; i < noOfChars * 2; i++)
		{
			chars.push_back(65 + ((qreal) qrand() / RAND_MAX) * (90 - 65));
			if (!allCapital) chars.push_back(97 + ((qreal) qrand() / RAND_MAX) * (122 - 97));
			if (includeNumbers) chars.push_back(48 + ((qreal) qrand() / RAND_MAX) * (57 - 48));
			if (includeSymbols) chars.push_back(33 + ((qreal) qrand() / RAND_MAX) * (47 - 33));
		}

		for (int i = 0; i < noOfChars; i++)
		{
			text += chars[(qrand() / (qreal) RAND_MAX) * (chars.size() - 1.0)];
		}

		m_captchaText = text;
	}
	else if (m_textGeneration == TextGeneration_Dictionary)
	{
		if (m_dictionary.size() <= 5)
		{
			qWarning() << "In text generation : Dictionary size is too small";
			return;
		}
		m_captchaText = m_dictionary[(qrand() / (qreal) RAND_MAX) * (m_dictionary.size() - 1.0)];
	}
	else
	{
		qWarning() << "Unable to generate text : Invalid text generation mode";
	}	
	updateCaptcha();
}
