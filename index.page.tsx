import React from "react";
import styled from "styled-components";
import tutorialsIcon from "./assets/site/icons/tutorials.svg";
import onboardingIcon from "./assets/site/icons/onboarding.svg";
import resourcesIcon from "./assets/site/icons/resources.svg";
import { ArrowRightIcon, Button } from "@redocly/theme";
import { Cards } from "@redocly/theme/markdoc/components/Cards/Cards";

type CardWithCodeProps = {
  url: string;
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
  border-radius: 12px;
  transition: transform 0.2s, box-shadow 0.2s;
  margin-bottom: 0;
  position: relative;
  min-height: 120px;
  max-width: 340px;
  width: 100%;
  border: 1px solid var(--border-color, #23272f);
  box-shadow: 0 4px 16px rgba(0,0,0,0.13);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;

  &:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 8px 24px rgba(0,0,0,0.18);
  }

  .hidden-link {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }
`;

const TopRow = styled.div`
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 6px;

  img {
    width: 28px;
    height: 28px;
  }

  h4 {
    margin: 0;
    color: var(--text-color);
    font-size: 18px;
    font-weight: 600;
  }
`;

const Description = styled.p`
  margin: 0;
  color: var(--text-color-secondary);
  font-size: 15px;
  line-height: 22px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  max-height: 44px;
`;

export const DlCard = ({ url, title, description, icon, onClick }: CardWithCodeProps) => {
  return (
    <CardWrapper onClick={onClick}>
      <a href={url} className="hidden-link" aria-hidden="true">{title}</a>
      <TopRow>
        <img src={icon} alt={title} />
        <h4>{title}</h4>
      </TopRow>
      <Description>{description}</Description>
    </CardWrapper>
  );
};

const CardsGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px 24px;
  margin-top: 2rem;
  width: 100%;
  max-width: 760px;
  margin-left: auto;
  margin-right: auto;
  justify-items: center;
  justify-content: center;

  @media (max-width: 700px) {
    grid-template-columns: 1fr;
    max-width: 95vw;
  }
`;

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
            <CardsGrid>
                <DlCard
                    title="Tutorials"
                    description="Level up your skills with our hands-on guides! From basics to advanced AI wizardry"
                    icon={tutorialsIcon}
                    onClick={() => window.location.href = '/tutorials'}
                    url='/tutorials'    
                />
                <DlCard
                    title="Notebooks"
                    description="Run end to end use cases with Jupyter Notebooks"
                    icon={tutorialsIcon}
                    onClick={() => window.location.href = '/notebooks/notebooks'}
                    url='/notebooks/notebooks'
                />
                <DlCard
                    title="Onboarding"
                    description="Zero to hero: Your fast track to mastering the Dataloop platform "
                    icon={onboardingIcon}
                    onClick={() => window.location.href = '/onboarding/onboarding'}
                    url='/onboarding/onboarding'
                />
                <DlCard
                    title="Resources"
                    description="Your toolbox of SDKs, APIs, and developer goodies to build something amazing"
                    icon={resourcesIcon}
                    onClick={() => window.location.href = '/resources'}
                    url='/resources'
                />
            </CardsGrid>
        </Container>
    );
}
