import React from "react";
import styled from "styled-components";
import tutorialsIcon from "./assets/site/icons/tutorials.svg";
import onboardingIcon from "./assets/site/icons/onboarding.svg";
import resourcesIcon from "./assets/site/icons/resources.svg";
import { ArrowRightIcon, Button } from "@redocly/theme";
import { Cards } from "@redocly/theme/markdoc/components/Cards/Cards";

type CardWithCodeProps = {
  title: string;
  description: string;
  icon: string;
  onClick: () => void;
};

const Container = styled.div`
    padding: 2rem;
`;

const Header = styled.div`
    text-align: center;
    margin-bottom: 3rem;
`;

const Title = styled.h1`
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: var(--text-color);
`;

const Subtitle = styled.h2`
    font-size: 1.5rem;
    font-weight: normal;
    margin-bottom: 2rem;
    color: var(--text-color-secondary);
`;

const CardWrapper = styled.div`
  cursor: pointer;
  padding: 16px;
  background-color: var(--layer-color-ontonal);
  border-radius: 8px;
  transition: transform 0.2s, box-shadow 0.2s;
  margin-bottom: 16px;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
`;

const TopRow = styled.div`
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;

  img {
    width: 32px;
    height: 32px;
  }

  h4 {
    margin: 0;
    color: var(--text-color);
    font-size: 20px;
    font-weight: 600;
  }
`;

const Description = styled.p`
  margin: 0;
  color: var(--text-color-secondary);
  font-size: 16px;
  line-height: 24px;
`;

export const DlCard = ({ title, description, icon, onClick }: CardWithCodeProps) => {
  return (
    <CardWrapper onClick={onClick}>
      <TopRow>
        <img src={icon} alt={title} />
        <h4>{title}</h4>
      </TopRow>
      <Description>{description}</Description>
    </CardWrapper>
  );
};

export default function HomePage() {
    return (
        <Container>
            <Header>
                <Title>Welcome to Dataloop's Developer Hub! 🚀</Title>
                <Subtitle>
                    Your launchpad for building amazing AI-powered applications
                </Subtitle>
                <Button
                    variant="outlined"
                    size="xlarge"
                    to="/tutorials/getting_started/sdk_overview/chapter"
                >
                    Start Your Journey <ArrowRightIcon />
                </Button>
            </Header>
            <Cards>
                <DlCard
                    title="Tutorials"
                    description="Level up your skills with our hands-on guides! From basics to advanced AI wizardry"
                    icon={tutorialsIcon}
                    onClick={() => window.location.href = '/tutorials'}
                />
                <DlCard
                    title="Onboarding"
                    description="Zero to hero: Your fast track to mastering the Dataloop platform "
                    icon={onboardingIcon}
                    onClick={() => window.location.href = '/onboarding/onboarding'}
                />
                <DlCard
                    title="Resources"
                    description="Your toolbox of SDKs, APIs, and developer goodies to build something amazing"
                    icon={resourcesIcon}
                    onClick={() => window.location.href = '/resources'}
                />
            </Cards>
        </Container>
    );
}
